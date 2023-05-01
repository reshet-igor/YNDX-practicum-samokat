#Связываем все файлы
import configuration
import requests
import data


#Создаем новый заказ
def new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body) #из конфига и даты подтягиваем актуальные данные

#Сохраняем трек-номер
def save_track():
    order_response = new_order() #берем информацию из прошлой функции
    current_order = order_response.json().copy() #копируем оттуда ответ
    current_order["t"] = current_order["track"] #забираем нужный нам номер
    current_order.pop("track") #избавляемся от лишнего
    return current_order #возвращаем обновленную переменную

#Получаем заказ по треку
def order_by_track():
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK,
                        params=save_track()) #получаем запрос

response = order_by_track() #сохраняем ответ который пойдет в автотест

def test_auto():
    # проверяем правильность ответа
    assert response.status_code == 200