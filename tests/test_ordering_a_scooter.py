import pytest
import allure
from data_order import OrderData
from pages.ordering_a_scooter_page import OrderPage


@allure.feature("Заказ самоката")
class TestOrderScooter:

    @pytest.mark.parametrize("order_data", OrderData.get_order_data())
    @allure.title("Позитивный сценарий заказа самоката")
    def test_order_scooter_positive_flow(self, driver, order_data):
        order_page = OrderPage(driver)

        with allure.step(f"Нажимаем на кнопку заказа ({order_data['order_button']})"):
            order_page.click_order_button(order_data["order_button"])

        with allure.step("Заполняем личные данные пользователя"):
            order_page.fill_personal_info(
                order_data["name"],
                order_data["last_name"],
                order_data["address"],
                order_data["metro_station"],
                order_data["phone"]
            )

        with allure.step("Заполняем данные аренды"):
            order_page.fill_rental_info(
                order_data["delivery_date"],
                order_data["rental_period"],
                order_data["color"],
                order_data.get("comment")
            )

        with allure.step("Подтверждаем заказ"):
            order_page.confirm_order()

        with allure.step("Проверяем, что заказ успешно оформлен"):
            success_message = order_page.get_success_message()
            allure.attach(success_message, name="Текст модалки", attachment_type=allure.attachment_type.TEXT)
            assert "Заказ оформлен" in success_message

        with allure.step("Проверяем, что отображается номер заказа"):
            order_number = order_page.get_order_number()
            allure.attach(order_number, name="Номер заказа", attachment_type=allure.attachment_type.TEXT)
            assert "Номер заказа" in order_number

        with allure.step("Кликаем на кнопку 'Посмотреть статус'"):
            order_page.click_view_status()