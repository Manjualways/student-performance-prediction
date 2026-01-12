import pandas as pd
import joblib

try:
    path = r"C:\Users\gopan\OneDrive\Desktop\New folder2\student performance\model\student_model.pkl"
    print(f"Attempting to load from: {path}")
   
    try:
        data = pd.read_pickle(path)
        print("Loaded as pandas pickle.")
        print(type(data))
        print(data.head())
    except Exception as e:
        print(f"Not a pandas pickle: {e}")
        
        
        try:
            data = joblib.load(path)
            print("Loaded with joblib.")
            print(type(data))
        except Exception as e2:
            print(f"Not a joblib file: {e2}")

except Exception as e:
    print(f"Error: {e}")
