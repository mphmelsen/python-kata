import datetime
import unittest
from unittest.mock import patch
from uuid import uuid4

from src.main import determine_average_feedback_after_certain_time
from src.main import determine_average_ride_duration_minute_per_taxi
from src.main import determine_taxi_with_best_feedback


class TestMain(unittest.TestCase):
    @patch("src.main.get_all_rides")
    def test_determine_average_ride_duration_minute_per_taxi(self, mocked_get_all_rides):
        mocked_get_all_rides.return_value = iter([
            {
                "companyId": 1,
                "taxiId": 1000,
                "rideId": str(uuid4()),
                "rideStart": 0,
                "rideEnd": 5 * 60 * 1000,
                "feedbackAmountOfStars": 3
            },
            {
                "companyId": 1,
                "taxiId": 1000,
                "rideId": str(uuid4()),
                "rideStart": 0,
                "rideEnd": 10 * 60 * 1000,
                "feedbackAmountOfStars": 3
            },
            {
                "companyId": 1,
                "taxiId": 1001,
                "rideId": str(uuid4()),
                "rideStart": 0,
                "rideEnd": 10 * 60 * 1000,
                "feedbackAmountOfStars": 3
            },
            {
                "companyId": 1,
                "taxiId": 1001,
                "rideId": str(uuid4()),
                "rideStart": 0,
                "rideEnd": 50 * 60 * 1000,
                "feedbackAmountOfStars": 3
            }
        ])

        expected_result = {
            1000: 8.0,
            1001: 30.0
        }

        self.assertEqual(expected_result, determine_average_ride_duration_minute_per_taxi())

    @patch('src.main.get_all_rides')
    def test_determine_taxi_with_best_feedback(self, mocked_get_all_rides):
        mocked_get_all_rides.return_value = iter([
            {
                "companyId": 1,
                "taxiId": 1000,
                "rideId": str(uuid4()),
                "rideStart": 0,
                "rideEnd": 5 * 60 * 1000,
                "feedbackAmountOfStars": 3
            },
            {
                "companyId": 1,
                "taxiId": 1002,
                "rideId": str(uuid4()),
                "rideStart": 0,
                "rideEnd": 5 * 60 * 1000,
                "feedbackAmountOfStars": 1
            }
        ])

        expected_result = (1000, 3)

        self.assertEqual(expected_result, determine_taxi_with_best_feedback())

    @patch("src.main.get_all_rides")
    def test_determine_average_feedback_after_certain_time(self, mocked_get_all_rides):
        mocked_get_all_rides.return_value = iter([
            {
                "companyId": 1,
                "taxiId": 1000,
                "rideId": str(uuid4()),
                "rideStart": int(datetime.datetime(year=2020, month=11, day=1, hour=22, minute=30, second=23, microsecond=0).timestamp() * 1000),
                "rideEnd": int(datetime.datetime(year=2020, month=11, day=1, hour=23, minute=58, second=2, microsecond=0).timestamp() * 1000),
                "feedbackAmountOfStars": 3
            },
            {
                "companyId": 1,
                "taxiId": 1000,
                "rideId": str(uuid4()),
                "rideStart": int(datetime.datetime(year=2020, month=11, day=1, hour=10, minute=30, second=23,
                                                   microsecond=0).timestamp() * 1000),
                "rideEnd": int(datetime.datetime(year=2020, month=11, day=1, hour=11, minute=58, second=2,
                                                 microsecond=0).timestamp() * 1000),
                "feedbackAmountOfStars": 5
            }
        ])

        expected_result = 3.0

        self.assertEqual(expected_result, determine_average_feedback_after_certain_time())
