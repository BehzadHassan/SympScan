from flask import Flask, request, jsonify
from Model.Predict import get_details
from flask_cors import CORS

app = Flask(__name__)
from flask_cors import CORS

CORS(app)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    symptoms = data['symptomsList']
    print(symptoms)

    try:
        result = get_details(symptoms)  # call your prediction logic
        print(result)
        return jsonify({'status': 'success', 'result': result})
    except Exception as e:
        print(str(e))
        return jsonify({'status': 'error', 'message': str(e)}), 500
