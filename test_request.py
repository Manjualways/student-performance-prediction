import requests
import json

url = "http://127.0.0.1:5000/predict"
data = {
    "attendance": 85,
    "study_hours": 5,
    "previous_score": 75
}

try:
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")
