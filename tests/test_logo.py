# tests/test_logo.py
import allure
from pages.logo_page import LogoPage

@allure.feature("Переход по логотипам")
class TestLogos:

    @allure.title("Проверка: клик по логотипу 'Самокат' ведет на главную страницу")
    def test_scooter_logo_redirects_to_main_page(self, driver):
        page = LogoPage(driver)

        page.open_main_page()
        page.click_scooter_logo()

        current_url = page.get_current_url()
        allure.attach(current_url, name="Фактический URL", attachment_type=allure.attachment_type.TEXT)

        assert "qa-scooter.praktikum-services.ru" in current_url, \
            f"Ожидали переход на qa-scooter.praktikum-services.ru, получили {current_url}"

    @allure.title("Проверка: клик по логотипу 'Яндекс' ведет на Dzen (новое окно)")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        page = LogoPage(driver)

        page.open_main_page()
        page.click_yandex_logo()
        page.switch_to_new_window("dzen.ru")

        current_url = page.get_current_url()
        allure.attach(current_url, name="Фактический URL", attachment_type=allure.attachment_type.TEXT)
    
        assert "dzen.ru" in current_url, \
            f"Ожидали переход на dzen.ru, получили {current_url}"
