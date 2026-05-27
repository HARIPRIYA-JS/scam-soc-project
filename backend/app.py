from flask import Flask, request, jsonify, render_template
import joblib
from pymongo import MongoClient
import os

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

    return render_template(
        "result.html",
        url=msg,
        prediction=str(result).lower()
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0", port=port)
