import numpy as np
from sklearn.linear_model import LinearRegression

class CoursePredictor:
    def __init__(self):
        self.model = LinearRegression()
        # Train on mock data immediately for simplicity
        self._train_model()
        
    def _train_model(self):
        # Mock data
        # Feature 1: Study hours per week, Feature 2: Previous GPA
        # Target: Final Grade Expected (0-100)
        X = np.array([
            [2, 2.0],
            [5, 2.5],
            [10, 3.0],
            [15, 3.5],
            [20, 3.8],
            [25, 4.0]
        ])
        y = np.array([55, 65, 75, 85, 92, 98])
        self.model.fit(X, y)
        
    def predict_grade(self, study_hours, previous_gpa):
        if study_hours < 0 or previous_gpa < 0 or previous_gpa > 4.0:
            raise ValueError("Invalid input values")
            
        prediction = self.model.predict(np.array([[study_hours, previous_gpa]]))
        # Clamp between 0 and 100
        return max(0, min(100, round(prediction[0], 2)))

def calculate_gpa(grades):
    """
    Given a list of grade percentages (0-100), calculates a standard 4.0 scale GPA.
    Standard scale mock: A=4.0(>90), B=3.0(>80), C=2.0(>70), D=1.0(>60), F=0(<60)
    """
    if not grades:
        return 0.0
        
    points = 0.0
    for grade in grades:
        if grade >= 90:
            points += 4.0
        elif grade >= 80:
            points += 3.0
        elif grade >= 70:
            points += 2.0
        elif grade >= 60:
            points += 1.0
            
    return round(points / len(grades), 2)
