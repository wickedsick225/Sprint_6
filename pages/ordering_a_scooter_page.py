import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators.ordering_a_scooter_locators import OrderLocators


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Кликаем на кнопку 'Заказать' ({button_type})")
    def click_order_button(self, button_type):
        locator = OrderLocators.ORDER_BUTTON_TOP if button_type == "top" else OrderLocators.ORDER_BUTTON_BOTTOM
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Заполняем личные данные: {name} {surname}, адрес {address}, метро {metro}, телефон {phone}")
    def fill_personal_info(self, name, surname, address, metro, phone):
        with allure.step("Принимаем cookies, если кнопка есть"):
            try:
                WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable(OrderLocators.COOKIES_ACCEPT_BUTTON)
                ).click()
            except Exception:
                pass

        with allure.step("Вводим имя, фамилию и адрес"):
            self.driver.find_element(*OrderLocators.NAME_INPUT).send_keys(name)
            self.driver.find_element(*OrderLocators.SURNAME_INPUT).send_keys(surname)
            self.driver.find_element(*OrderLocators.ADDRESS_INPUT).send_keys(address)

        with allure.step(f"Выбираем станцию метро: {metro}"):
            metro_input = self.driver.find_element(*OrderLocators.METRO_INPUT)
            metro_input.send_keys(metro)
            try:
                metro_option = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class,'select-search__option') and text()='{metro}']"))
                )
                metro_option.click()
            except Exception:
                fallback_option = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".select-search__option"))
                )
                fallback_option.click()
            metro_input.send_keys(Keys.ESCAPE)

        with allure.step("Вводим телефон и продолжаем оформление"):
            self.driver.find_element(*OrderLocators.PHONE_INPUT).send_keys(phone)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(OrderLocators.CONTINUE_BTN)
            ).click()

    @allure.step("Заполняем данные аренды: дата {delivery_date}, срок {rental_period}, цвет {color}, комментарий {comment}")
    def fill_rental_info(self, delivery_date, rental_period, color, comment=None):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderLocators.HEAD_TEXT_ORDER)
        )

        with allure.step(f"Выбираем дату доставки: {delivery_date}"):
            date_input = self.driver.find_element(*OrderLocators.DATE_INPUT)
            date_input.click()
            date_option_locator = (OrderLocators.DATE_OPTION[0], OrderLocators.DATE_OPTION[1].format(delivery_date))
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(date_option_locator)
            ).click()

        with allure.step(f"Выбираем срок аренды: {rental_period}"):
            term_dropdown = self.driver.find_element(*OrderLocators.TERM_DROPDOWN)
            term_dropdown.click()
            term_option_locator = (OrderLocators.TERM_OPTION[0], OrderLocators.TERM_OPTION[1].format(rental_period))
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(term_option_locator)
            ).click()

        with allure.step(f"Выбираем цвет самоката: {color}"):
            color_checkbox = self.driver.find_element(
                *OrderLocators.COLOR_BLACK if color == "black" else OrderLocators.COLOR_GREY
            )
            color_checkbox.click()

        if comment:
            with allure.step(f"Добавляем комментарий: {comment}"):
                self.driver.find_element(*OrderLocators.COMMENT_INPUT).send_keys(comment)

        self.driver.find_element(*OrderLocators.ORDER_CONFIRM_BUTTON).click()

    @allure.step("Подтверждаем заказ")
    def confirm_order(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderLocators.CONFIRM_MODAL_TEXT)
        )
        yes_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderLocators.YES_BUTTON)
        )
        yes_button.click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderLocators.SUCCESS_MODAL_HEADER)
        )

    @allure.step("Получаем сообщение об успешном заказе")
    def get_success_message(self):
        message = self.driver.find_element(*OrderLocators.SUCCESS_MODAL_HEADER).text
        allure.attach(message, name="Текст подтверждения", attachment_type=allure.attachment_type.TEXT)
        return message

    @allure.step("Получаем номер заказа")
    def get_order_number(self):
        order_number = self.driver.find_element(*OrderLocators.SUCCESS_ORDER_NUMBER).text
        allure.attach(order_number, name="Номер заказа", attachment_type=allure.attachment_type.TEXT)
        return order_number

    @allure.step("Открываем статус заказа")
    def click_view_status(self):
        self.driver.find_element(*OrderLocators.SUCCESS_VIEW_STATUS_BUTTON).click()