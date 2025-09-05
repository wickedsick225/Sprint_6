import allure
import pytest
from pages.important_questions_page import ImportantQuestionsPage
from locators.important_questions_locators import ImportantQuestionsLocators
from data import ImportantQuestionsTexts

@allure.suite("FAQ")
class TestImportantQuestions:

    @pytest.mark.parametrize("question_locator, answer_locator, expected_text", [
        (ImportantQuestionsLocators.question_price_scooter, ImportantQuestionsLocators.question_price_scooter_text, ImportantQuestionsTexts.PRICE_SCOOTER),
        (ImportantQuestionsLocators.question_time_scooter, ImportantQuestionsLocators.question_time_scooter_text, ImportantQuestionsTexts.TIME_SCOOTER),
        (ImportantQuestionsLocators.question_multiple_scooter, ImportantQuestionsLocators.question_multiple_scooter_text, ImportantQuestionsTexts.MULTIPLE_SCOOTER),
        (ImportantQuestionsLocators.question_order_scooter_today, ImportantQuestionsLocators.question_order_scooter_today_text, ImportantQuestionsTexts.ORDER_SCOOTER_TODAY),
        (ImportantQuestionsLocators.question_extend_scooter, ImportantQuestionsLocators.question_extend_scooter_text, ImportantQuestionsTexts.EXTEND_SCOOTER),
        (ImportantQuestionsLocators.question_charge_scooter, ImportantQuestionsLocators.question_charge_scooter_text, ImportantQuestionsTexts.CHARGE_SCOOTER),
        (ImportantQuestionsLocators.question_cancel_order, ImportantQuestionsLocators.question_cancel_order_text, ImportantQuestionsTexts.CANCEL_ORDER),
        (ImportantQuestionsLocators.question_mkad_scooter, ImportantQuestionsLocators.question_mkad_scooter_text, ImportantQuestionsTexts.MKAD_SCOOTER),
    ])
    @allure.title("Проверка FAQ: текст ответа совпадает с ожидаемым")
    def test_important_questions(self, driver, question_locator, answer_locator, expected_text):
        with allure.step("Открываем страницу с вопросами"):
            questions_page = ImportantQuestionsPage(driver)
            questions_page.open_page()

        with allure.step("Кликаем по вопросу и получаем текст ответа"):
            actual_text = questions_page.click_question_and_get_answer(question_locator, answer_locator)

        with allure.step("Сравниваем текст ответа с ожидаемым"):
            assert actual_text == expected_text, f"Ожидали: {expected_text}, получили: {actual_text}"