import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.important_questions_locators import ImportantQuestionsLocators
from pages.base_urls import URLS

class ImportantQuestionsTexts:
    PRICE_SCOOTER = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    TIME_SCOOTER = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    MULTIPLE_SCOOTER = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    ORDER_SCOOTER_TODAY = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    EXTEND_SCOOTER = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    CHARGE_SCOOTER = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    CANCEL_ORDER = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    MKAD_SCOOTER = "Да, обязательно. Всем самокатов! И Москве, и Московской области."

class ImportantQuestionsPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем главную страницу приложения")
    def open_page(self):
        self.driver.get(URLS.BASE_URL)

    @allure.step("Кликаем на вопрос и получаем ответ")
    def click_question_and_get_answer(self, question_locator, answer_locator):
        with allure.step("Скроллим страницу до вопроса и кликаем на него"):
            question_element = self.driver.find_element(*question_locator)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question_element)
            question_element.click()

        with allure.step("Ожидаем появления текста ответа"):
            answer_element = WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(*answer_locator) if d.find_element(*answer_locator).text.strip() != "" else False
            )
        return answer_element.text