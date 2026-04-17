from flask import Flask, request, jsonify, render_template
from logic.calculator import CoursePredictor, calculate_gpa
import os

app = Flask(__name__)
predictor = CoursePredictor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        study_hours = float(data.get('study_hours', 0))
        previous_gpa = float(data.get('previous_gpa', 0))
        
        predicted_grade = predictor.predict_grade(study_hours, previous_gpa)
        return jsonify({'predicted_grade': predicted_grade, 'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'error'}), 400

@app.route('/api/calculate_gpa', methods=['POST'])
def get_gpa():
    try:
        data = request.get_json()
        grades = data.get('grades', [])
        # Ensure list of floats
        grades = [float(g) for g in grades]
        
        gpa = calculate_gpa(grades)
        return jsonify({'gpa': gpa, 'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'error'}), 400

if __name__ == '__main__':
    # Run server locally
    app.run(host='127.0.0.1', port=5000, debug=True)
