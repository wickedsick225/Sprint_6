import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from locators.ordering_a_scooter_locators import OrderLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Кликаем на кнопку 'Заказать' ({button_type})")
    def click_order_button(self, button_type):
        locator = OrderLocators.ORDER_BUTTON_TOP if button_type == "top" else OrderLocators.ORDER_BUTTON_BOTTOM
        element = self.scroll_into_view(locator)
        self.wait_for_visible(locator).click()
        return element

    @allure.step("Заполняем личные данные: {name} {surname}, адрес {address}, метро {metro}, телефон {phone}")
    def fill_personal_info(self, name, surname, address, metro, phone):
        with allure.step("Принимаем cookies, если кнопка есть"):
            try:
                self.click(OrderLocators.COOKIES_ACCEPT_BUTTON, timeout=3)
            except TimeoutException:
                pass

        with allure.step("Вводим имя, фамилию и адрес"):

            self.send_keys(OrderLocators.NAME_INPUT, name)
            self.send_keys(OrderLocators.SURNAME_INPUT, surname)
            self.send_keys(OrderLocators.ADDRESS_INPUT, address)

        with allure.step(f"Выбираем станцию метро: {metro}"):
            self.send_keys(OrderLocators.METRO_INPUT, metro)

            try:
                metro_option = self.find_element(
                    (By.XPATH, f"//div[contains(@class,'select-search__option') and text()='{metro}']"), 
                    timeout=5
                )
                self.click((By.XPATH, f"//div[contains(@class,'select-search__option') and text()='{metro}']"))
            except TimeoutException:
                self.click((By.CSS_SELECTOR, ".select-search__option"), timeout=5)

            self.press_key(OrderLocators.METRO_INPUT, Keys.ESCAPE)

        with allure.step("Вводим телефон и продолжаем оформление"):
            self.send_keys(OrderLocators.PHONE_INPUT, phone)
            self.click(OrderLocators.CONTINUE_BTN)

    @allure.step("Заполняем данные аренды: дата {delivery_date}, срок {rental_period}, цвет {color}, комментарий {comment}")
    def fill_rental_info(self, delivery_date, rental_period, color, comment=None):
        self.wait_for_visible(OrderLocators.HEAD_TEXT_ORDER)

        with allure.step(f"Выбираем дату доставки: {delivery_date}"):
            date_input = self.find_element(OrderLocators.DATE_INPUT)
            date_input.click()
            date_option_locator = (OrderLocators.DATE_OPTION[0], OrderLocators.DATE_OPTION[1].format(delivery_date))
            self.click(date_option_locator)

        with allure.step(f"Выбираем срок аренды: {rental_period}"):
            term_dropdown = self.find_element(OrderLocators.TERM_DROPDOWN)
            term_dropdown.click()
            term_option_locator = (OrderLocators.TERM_OPTION[0], OrderLocators.TERM_OPTION[1].format(rental_period))
            self.click(term_option_locator)

        with allure.step(f"Выбираем цвет самоката: {color}"):
            color_checkbox = self.find_element(
                OrderLocators.COLOR_BLACK if color == "black" else OrderLocators.COLOR_GREY
            )
            color_checkbox.click()

        if comment:
            with allure.step(f"Добавляем комментарий: {comment}"):
                self.send_keys(OrderLocators.COMMENT_INPUT, comment)

        self.click(OrderLocators.ORDER_CONFIRM_BUTTON)

    @allure.step("Подтверждаем заказ")
    def confirm_order(self):
        self.wait_for_visible(OrderLocators.CONFIRM_MODAL_TEXT)
        self.click(OrderLocators.YES_BUTTON)
        self.wait_for_visible(OrderLocators.SUCCESS_MODAL_HEADER)

    @allure.step("Получаем сообщение об успешном заказе")
    def get_success_message(self):
        message = self.get_text(OrderLocators.SUCCESS_MODAL_HEADER)
        allure.attach(message, name="Текст подтверждения", attachment_type=allure.attachment_type.TEXT)
        return message

    @allure.step("Получаем номер заказа")
    def get_order_number(self):
        order_number = self.get_text(OrderLocators.SUCCESS_ORDER_NUMBER)
        allure.attach(order_number, name="Номер заказа", attachment_type=allure.attachment_type.TEXT)
        return order_number

    @allure.step("Открываем статус заказа")
    def view_status(self):
        self.click(OrderLocators.SUCCESS_VIEW_STATUS_BUTTON)
