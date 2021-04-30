from flask import Flask, jsonify
from flask_cors import CORS

from app.errors import InvalidRequest, InternalError

app = Flask(__name__)
CORS(app)

'''
ERROS PADRÕES
'''
@app.errorhandler(InvalidRequest)
def handle_bad_request(err):
    resp = jsonify(err.to_dict())
    resp.status_code = err.status_code
    return resp

@app.errorhandler(InternalError)
def handle_bad_request(err):
    resp = jsonify(err.to_dict())
    resp.status_code = err.status_code
    return resp


'''
IMPORTANDO ROTAS DA API
'''
from app.routes import root, predict
