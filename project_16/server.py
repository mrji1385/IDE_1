from flask import Flask, request, jsonify
import pickle
import numpy as np

# Загружаем модель из файла и десериализуем ее
with open('model.pkl', 'rb') as pkl_file: 
    model = pickle.load(pkl_file)

app = Flask(__name__)

@app.route('/')
def index():
    message = """Сервер работает. 
    Пожалуйста, запустите файл client.py для получения прогноза."""
    return message

@app.route('/predict', methods=['POST'])
def predict():
    # Получаем запрос от клиента и выполняем предсказание
    features = np.array(request.json).reshape(1, -1)
    prediction = round(model.predict(features)[0])
    # Возвращаем предсказание
    return  jsonify({'prediction': prediction})

if __name__ == '__main__':
    
    app.run('localhost', 5000)