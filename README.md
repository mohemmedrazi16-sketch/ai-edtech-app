# AI EdTech CI/CD Web Application

A beautiful, premium AI-enhanced web application built with Python (Flask) and Vanilla CSS. It provides a simple GPA calculator and an AI grade predictor utilizing `scikit-learn`.

## Features
- **Premium Frontend:** Deeply styled glassmorphism Aesthetic with Vanilla CSS, no heavy UI frameworks.
- **REST API:** Modular backend with endpoints (`/api/calculate_gpa`, `/api/predict`).
- **Machine Learning Integration:** Uses basic Linear Regression trained on hypothetical study metrics.
- **CI/CD Built-In:** Ready-made `.github/workflows/ci.yml` and `Jenkinsfile` for seamless DevOps portfolio demonstration.
- **Unit Testing:** Full `unittest` test suite encompassing system logic.

## Setup Instructions

Ensure you have Python 3.10+ installed.

1. **Initialize Virtual Environment**
   ```bash
   python -m venv venv
   source venv/Scripts/activate   # On Windows use: venv\Scripts\activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Unit Tests (Optional)**
   ```bash
   python -m unittest discover tests -v
   ```

4. **Launch the Web Server**
   ```bash
   python app.py
   ```
   Open `http://127.0.0.1:5000` in your web browser.

## CI/CD Notes
- The test pipelines are designed to trigger immediately upon `push` to the main branch via GitHub Actions.
- Ensure your Jenkins setup points to this remote repository for the declarative `Jenkinsfile` to run.
