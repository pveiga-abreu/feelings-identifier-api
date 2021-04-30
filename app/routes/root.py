from flask import jsonify

from app import app

@app.route('/', methods=['GET'])
def root():
    return jsonify({
        "status": True,
        'message': 'API Online v0.1.0'
    })
