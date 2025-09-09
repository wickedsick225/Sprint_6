import allure
from pages.base_page import BasePage
from locators.logo_locators import LogoLocators
from pages.base_urls import URLS
from selenium.webdriver.support.ui import WebDriverWait



class LogoPage(BasePage):

    @allure.step("Открываем главную страницу сервиса")
    def open_main_page(self):
        self.open_url(URLS.BASE_URL)

    @allure.step("Кликаем по логотипу 'Самокат'")
    def click_scooter_logo(self):
        self.wait_for_clickable(LogoLocators.scooter_logo).click()

    @allure.step("Кликаем по логотипу 'Яндекс'")
    def click_yandex_logo(self):
        self.wait_for_clickable(LogoLocators.yandex_logo).click()

    def switch_to_new_window(self, expected_url_substring, timeout=10):
        self.wait_for_condition(lambda d: len(self.get_window_handles()) > 1, timeout=timeout)
        self.switch_to_window(-1)
        self.wait_for_condition(lambda d: expected_url_substring in self.get_current_url(), timeout=timeout)