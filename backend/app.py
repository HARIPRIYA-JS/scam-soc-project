from flask import Flask, request, jsonify
import joblib
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["scam_soc"]
collection = db["alerts"]

model = joblib.load('../model/scam_detector.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    msg = data['message']

    result = model.predict([msg])[0]

    collection.insert_one({
        "message": msg,
        "prediction": result
    })

    return jsonify({'prediction': result})

app.run(host='0.0.0.0', port=5000)
