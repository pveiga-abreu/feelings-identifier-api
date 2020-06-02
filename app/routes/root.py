from flask import jsonify

from app import app

@app.route('/ai/predict', methods=['GET'])
def root():
    return jsonify({
        "status": "API Online v1"
    })
