import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from locators.logo_locators import LogoLocators
from pages.base_urls import URLS

@pytest.mark.parametrize("logo_locator, expected_domain, new_window", [
    (LogoLocators.scooter_logo, "qa-scooter.praktikum-services.ru", False),
    (LogoLocators.yandex_logo, "dzen.ru", True),
])


@allure.title("Проверка перехода по логотипам")
def test_logos(driver, logo_locator, expected_domain, new_window):
    with allure.step("Открываем главную страницу сервиса"):
        driver.get(URLS.BASE_URL)

    with allure.step(f"Кликаем по логотипу и проверяем переход на {expected_domain}"):
        driver.find_element(*logo_locator).click()

        if new_window:
            with allure.step("Ожидаем открытия нового окна и переключаемся в него"):
                WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
                driver.switch_to.window(driver.window_handles[-1])

        with allure.step("Ждём пока URL обновится и проверяем домен"):
            WebDriverWait(driver, 10).until(lambda d: expected_domain in d.current_url)
            current_url = driver.current_url
            allure.attach(current_url, name="Фактический URL", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Проверка: фактический URL содержит ожидаемый домен"):
        assert expected_domain in current_url, f"Ожидали домен {expected_domain}, получили {current_url}"