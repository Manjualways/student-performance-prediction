import joblib
import pandas as pd
import os

path = r"model/student_model.pkl"

if os.path.exists(path):
    try:
        obj = joblib.load(path)
        print(f"Loaded object type: {type(obj)}")
        print(f"Object content: {obj}")
    except Exception as e:
        print(f"Failed to load: {e}")
else:
    print("File not found")
