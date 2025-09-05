class OrderData:
    @staticmethod
    def get_order_data():
        return [
            {
                "order_button": "top",
                "name": "Иван",
                "last_name": "Иванов",
                "address": "ул. Ленина, д. 1",
                "metro_station": "Сокольники",
                "phone": "+79991234567",
                "delivery_date": "25-е сентября 2025",
                "rental_period": "двое суток",
                "color": "black",
                "comment": "Позвонить за час"
            },
            {
                "order_button": "bottom",
                "name": "Петр",
                "last_name": "Петров",
                "address": "пр. Мира, д. 10",
                "metro_station": "Красносельская",
                "phone": "+79997654321",
                "delivery_date": "26-е сентября 2025",
                "rental_period": "трое суток",
                "color": "grey",
                "comment": "Оставить у двери"
            }
        ]