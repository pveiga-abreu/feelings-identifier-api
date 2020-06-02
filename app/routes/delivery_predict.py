from flask import jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from app import app
from app.controllers.delivery_predict import make_predict

auth = HTTPBasicAuth()

user = {
    'usuario': generate_password_hash('senha')
}

@auth.verify_password
def verify_password(username, password):
    if (username in user and check_password_hash(user.get(username), password)):
        return username

@app.route('/ai/predict/delivery', methods=['POST'])
@auth.login_required
def predict():
    content = request.get_json()

    if len(content) != 7:
        return jsonify({
            "message": "Dados enviados incorretos"
            }), 400
    else:
        for key in content:
            if key not in ["unit", "product", "driver", "post_code", "list_hour", "weekday", "list_date"]:
                return jsonify({
                    "message": "Dados enviados incorretos"
                    }), 400
            
            if (key == "list_date") and not (type(content[key]) is str):
                return jsonify({
                    "message": "Dados enviados incorretos"
                    }), 400
            elif (key != "list_date") and not (type(content[key]) is int):
                return jsonify({
                    "message": "Dados enviados incorretos"
                    }), 400
            
    return make_predict(content)
