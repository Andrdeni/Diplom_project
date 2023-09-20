from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
import json

# загружаем модель из файла
with open('models/best_predictions_model.pkl', 'rb') as pkl_file:
    model = pickle.load(pkl_file)

# создаём приложение
app = Flask(__name__)

@app.route('/')
def index():
    msg = "Тестовое сообщение. Сервер запущен!"
    return msg

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
