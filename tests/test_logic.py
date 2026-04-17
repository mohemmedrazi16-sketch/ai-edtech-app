import unittest
from logic.calculator import calculate_gpa, CoursePredictor

class TestEdTechCalculator(unittest.TestCase):

    def test_calculate_gpa_basic(self):
        # A, B, C, D (4, 3, 2, 1 -> avg 2.5)
        grades = [95, 85, 75, 65]
        self.assertEqual(calculate_gpa(grades), 2.5)

    def test_calculate_gpa_empty(self):
        self.assertEqual(calculate_gpa([]), 0.0)

    def test_calculate_gpa_failing(self):
        grades = [50, 40]
        self.assertEqual(calculate_gpa(grades), 0.0)

class TestCoursePredictor(unittest.TestCase):

    def setUp(self):
        self.predictor = CoursePredictor()

    def test_predict_grade_positive(self):
        pred = self.predictor.predict_grade(15, 3.5)
        self.assertTrue(0 <= pred <= 100)
        self.assertGreater(pred, 70)  # General assumption based on mock data

    def test_predict_grade_invalid_input(self):
        with self.assertRaises(ValueError):
            self.predictor.predict_grade(-5, 3.0)
        
        with self.assertRaises(ValueError):
            self.predictor.predict_grade(10, 5.0)

if __name__ == '__main__':
    unittest.main()
