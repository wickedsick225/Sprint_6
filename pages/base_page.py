import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

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

    @allure.step("Получаем текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Получаем список окон")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Переключаемся на окно с индексом {index}")
    def switch_to_window(self, index=-1):
        self.driver.switch_to.window(self.driver.window_handles[index])

    @allure.step("Вводим текст '{value}' в элемент {locator}")
    def send_keys(self, locator, value, timeout=None):
        element = self.find_element(locator, timeout)
        element.send_keys(value)
        return element
    
        
    @allure.step("Нажимаем клавишу {key} в элементе {locator}")
    def press_key(self, locator, key, timeout=None):
        element = self.find_element(locator, timeout)
        element.send_keys(key)
        return element