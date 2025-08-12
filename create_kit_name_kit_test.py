# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data

# эта функция получает заказ по его номеру
def test_track_order():
    create_order = sender_stand_request.post_new_order(data.create_order_body)
    track = str(create_order.json()["track"])
    response = sender_stand_request.get_track_order(track)
    # Проверяется, что код ответа равен 200
    assert response.status_code == 200