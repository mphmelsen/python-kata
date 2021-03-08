import unittest

from src.main import determine_average_feedback_after_certain_time
from src.main import determine_average_ride_duration_minute_per_taxi
from src.main import determine_taxi_with_best_feedback
from unittest.mock import patch


class TestMain(unittest.TestCase):
    @patch("src.main.get_all_rides")
    def test_determine_average_ride_duration_minute_per_taxi(self, patched):
        patched.return_value = self.mocked_taxis()
        expected_result = {
            1000: 8.0,
            1001: 30.0
        }

        self.assertEqual(expected_result, determine_average_ride_duration_minute_per_taxi())

    @patch("src.main.get_all_rides")
    def test_determine_taxi_with_best_feedback(self, patched):
        patched.return_value = self.mocked_taxis()
        expected_result = (1000, 3)

        self.assertEqual(expected_result, determine_taxi_with_best_feedback())

    @patch("src.main.get_all_rides")
    def test_determine_average_feedback_after_certain_time(self, patched):
        patched.return_value = self.mocked_taxis()
        expected_result = 3.0

        self.assertEqual(expected_result, determine_average_feedback_after_certain_time())

    def mocked_taxis(self):
        return [
            {"companyId": 1, "taxiId": 1000, "rideId": "0001", "rideStart": 1612866728000, "rideEnd": 1612867208000, "feedbackAmountOfStars": 3},
            {"companyId": 1, "taxiId": 1001, "rideId": "0001", "rideStart": 1612906808000, "rideEnd": 1612908608000, "feedbackAmountOfStars": 3}
        ]
