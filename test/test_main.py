import unittest

from src.main import determine_average_feedback_after_certain_time
from src.main import determine_average_ride_duration_minute_per_taxi
from src.main import determine_taxi_with_best_feedback


class TestMain(unittest.TestCase):
    def test_determine_average_ride_duration_minute_per_taxi(self):
        expected_result = {
            1000: 8.0,
            1001: 30.0
        }

        self.assertEqual(expected_result, determine_average_ride_duration_minute_per_taxi())

    def test_determine_taxi_with_best_feedback(self):
        expected_result = (1000, 3)

        self.assertEqual(expected_result, determine_taxi_with_best_feedback())

    def test_determine_average_feedback_after_certain_time(self):
        expected_result = 3.0

        self.assertEqual(expected_result, determine_average_feedback_after_certain_time())
