from flask import Flask

app = Flask(__name__)

from app.routes import root, delivery_predict
