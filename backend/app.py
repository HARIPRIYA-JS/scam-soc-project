from flask import Flask, request, jsonify, render_template
import joblib
from pymongo import MongoClient

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
client = MongoClient("mongodb://localhost:27017/")
db = client["scam_soc"]
collection = db["alerts"]

model = joblib.load('model/scam_detector.pkl')

@app.route('/predict', methods=['POST'])
def predict():

    msg = request.form['message']

    result = model.predict([msg])[0]

    collection.insert_one({
        "message": msg,
        "prediction": str(result)
    })

    return f"""
    <h2>URL: {msg}</h2>
    <h1>Prediction: {result}</h1>
    <a href="/">Check Another URL</a>
    """
