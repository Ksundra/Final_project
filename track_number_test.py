import pendulum
import requests

import configuration
import data

# подставляю завтрашнюю дату в тело для создания заказа,
# чтобы данные для заказа соответствовали требованиям приложения
def change_order_body():
    tomorrow = pendulum.tomorrow("Europe/Moscow").format("YYYY-MM-DD")
    current_body = data.order_body.copy()
    current_body["deliveryDate"] = tomorrow
    return current_body


# запрос на создание заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=change_order_body(),
                         headers=data.headers)


# получение номера трека заказа
def get_new_order_track():
    return post_new_order().json()["track"]


# запрос на получение заказа по его трек-номеру
def get_order_info():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH
                        + "?t=" + str(get_new_order_track()),
                        headers=data.headers)


# проверка, что код ответа равен 200
def test_we_can_get_order_info():
    assert get_order_info().status_code == 200

# Новокщенова Ксения, 9-я когорта — Финальный проект. Финальная часть.
