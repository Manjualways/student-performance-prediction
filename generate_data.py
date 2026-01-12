import pandas as pd
import numpy as np

np.random.seed(42)
n_samples = 100

data = pd.DataFrame({
    'attendance': np.random.randint(50, 100, n_samples),
    'study_hours': np.random.randint(1, 10, n_samples),
    'previous_score': np.random.randint(40, 100, n_samples)
})

data['final_score'] = (
    0.3 * data['attendance'] + 
    2.5 * data['study_hours'] + 
    0.6 * data['previous_score'] + 
    np.random.normal(0, 5, n_samples)
).clip(0, 100)

data.to_csv('student_data.csv', index=False)
print("Created student_data.csv")
