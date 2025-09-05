import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout  

    @allure.step("Открываем страницу {url}")
    def open_url(self, url):
        self.driver.get(url)

    def wait_for_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Ищем элемент {locator}")
    def find_element(self, locator, timeout=None):
        if timeout is None:
            timeout = self.timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Кликаем по элементу {locator}")
    def click(self, locator, timeout=None):
        element = self.find_element(locator, timeout)
        element.click()
        return element

    @allure.step("Получаем текст элемента {locator}")
    def get_text(self, locator, timeout=None):
        return self.find_element(locator, timeout).text

    @allure.step("Скроллим к элементу {locator}")
    def scroll_into_view(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    @allure.step("Ждём пока элемент {locator} станет видимым")
    def wait_for_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )
    @allure.step('JS-клик по элементу')
    def js_click(self, locator, timeout=10):
        element = self.wait_for_visible(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ждём пока условие станет True")
    def wait_for_condition(self, condition_func, timeout=None):
        """Ожидает выполнения произвольной функции condition_func(driver) -> bool"""
        if timeout is None:
            timeout = self.timeout
        return WebDriverWait(self.driver, timeout).until(condition_func)
