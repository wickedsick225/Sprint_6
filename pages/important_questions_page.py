import allure
from pages.base_page import BasePage
from pages.base_urls import URLS

class ImportantQuestionsPage(BasePage):

    @allure.step("Открываем главную страницу приложения")
    def open_page(self):
        self.open_url(URLS.BASE_URL)

    @allure.step("Кликаем на вопрос и получаем ответ")
    def click_question_and_get_answer(self, question_locator, answer_locator):
        self.scroll_into_view(question_locator)
        self.js_click(question_locator)

        element = self.wait_for_visible(answer_locator)
        while element.text.strip() == "":
            element = self.wait_for_visible(answer_locator)

        return self.get_text(answer_locator)
