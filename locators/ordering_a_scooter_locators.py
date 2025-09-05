from selenium.webdriver.common.by import By

class OrderLocators:
    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH, "//button[text()='Заказать' and contains(@class, 'Button_Button__ra12g')]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")

    # Первая страница "Для кого самокат"
    HEAD_TEXT_AUTH = (By.XPATH, ".//div[text()='Для кого самокат']")
    NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    METRO_OPTION = (By.XPATH, "//div[contains(@class,'select-search__option') and text()='{}']")
    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    CONTINUE_BTN = (By.XPATH, "//button[contains(@class,'Button_Button') and text()='Далее']")
    COOKIES_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")

    # Вторая страница "Про аренду"
    HEAD_TEXT_ORDER = (By.XPATH, ".//div[text()='Про аренду']")
    DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    DATE_OPTION = (By.XPATH, "//div[contains(@aria-label,'{}')]")
    TERM_DROPDOWN = (By.XPATH, ".//div[@class='Dropdown-placeholder']")
    TERM_OPTION = (By.XPATH, "//div[text()='{}']")
    COLOR_BLACK = (By.XPATH, ".//input[@id='black']")
    COLOR_GREY = (By.XPATH, ".//input[@id='grey']")
    COMMENT_INPUT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    ORDER_CONFIRM_BUTTON = (By.XPATH,"//div[contains(@class,'Order_Buttons__1xGrp')]//button[text()='Заказать']")    

    # Модалка подтверждения
    CONFIRM_MODAL_TEXT = (By.XPATH, "//div[contains(text(), 'Хотите оформить заказ')]")
    YES_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[contains(text(), 'Да')]")
    NO_BUTTON = (By.XPATH, "//button[text()='Нет']")

    # Модалка успешного заказа
    SUCCESS_MODAL_HEADER = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")   # "Заказ оформлен"
    SUCCESS_ORDER_NUMBER = (By.CLASS_NAME, "Order_Text__2broi")          # "Номер заказа: ..."
    SUCCESS_VIEW_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
