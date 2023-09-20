import requests
import json



if __name__ == '__main__':
    
    # выполняем POST-запрос на сервер по эндпоинту add с параметром json
    r = requests.post('http://localhost:5000/predict', json=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1.0, 1.0, 1, 1.0, 1.0, 1])
    # выводим статус запроса
    print('churn: {}'.format(r.churn))
    # реализуем обработку результата
    if r.status_code == 200:
        # если запрос выполнен успешно (код обработки=200),
        # выводим результат на экран
        print('Prediction: {}'.format(r.json()['prediction']))
    else:
        # если запрос завершён с кодом, отличным от 200,
        # выводим содержимое ответа
        print(r.text)


