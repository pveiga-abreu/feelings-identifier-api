from datetime import datetime, timedelta
from flask import jsonify
from numpy import array
import pickle

model = pickle.load(open('app/model/model.pkl', 'rb'))

def make_predict(content):
    data = array([[content['unit'], content['product'], content['driver'], content['post_code'], content['list_hour'], content['weekday']]])
    prevision = int(round(model.predict(data)[0]))

    try:
        list_date = datetime.strptime(str(content['list_date'] + ' ' + str(content['list_hour']) + ':00'), '%Y-%m-%d %H:%M')
    except ValueError:
        return jsonify({
            "message": "Dados enviados incorretos"
            }), 400

    predicted_date = list_date + timedelta(hours=prevision)

    predicted_date = datetime.strftime(predicted_date, '%Y-%m-%d %H:%M')

    return jsonify({
        "entrega_prevista": predicted_date
        }), 200
