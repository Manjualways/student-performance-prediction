from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model/student_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        
        attendance = float(data["attendance"])
        study_hours = float(data["study_hours"])
        previous_score = float(data["previous_score"])
        
        prediction = model.predict([[attendance, study_hours, previous_score]])
        
        return jsonify({
            "Predicted Final Score": round(prediction[0], 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
