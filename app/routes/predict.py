from app.controllers import predict_controller

from app import app

@app.route('/predict', methods=['POST'])
def predict():
    return predict_controller.make_predict()
