import datetime
from collections import defaultdict
from math import ceil
from typing import Dict
from typing import Tuple

from src.imaginary_dynamodb_table import get_all_rides


def determine_average_ride_duration_minute_per_taxi() -> Dict[int, int]:
    # Determine the average ride duration in minutes per taxi given the rides returned by function below
    # Expected return format:
    # {
    #     <taxiId>: <averageRunDurationMinutesRoundedOff>,
    #     ...
    # }

    rides = get_all_rides()

    # Possible solution
    # Sort rides by taxiId
    rides_per_taxi = defaultdict(list)
    for ride in rides:
        rides_per_taxi[ride["taxiId"]].append(ride)

    # Calculate average duration per taxi
    taxi_duration = {}
    for taxi_id, rides in rides_per_taxi.items():
        average_duration_ms = sum([ride["rideEnd"] - ride["rideStart"] for ride in rides]) / len(rides)
        average_duration_minutes = ceil(average_duration_ms / 1000 / 60)

        taxi_duration[taxi_id] = average_duration_minutes

    return taxi_duration


def determine_taxi_with_best_feedback() -> Tuple[int, float]:
    # Determine the taxi that got the best feedback
    # Expected return format:
    # <taxiId>, <averageFeedback>

    rides = get_all_rides()

    # Possible solution
    # Sort rides by taxiId
    rides_per_taxi = defaultdict(list)
    for ride in rides:
        rides_per_taxi[ride["taxiId"]].append(ride)

    # Calculate feedback per taxiId
    taxi_feedback = {}
    for taxi_id, rides in rides_per_taxi.items():
        average_feedback = sum([ride["feedbackAmountOfStars"] for ride in rides]) / len(rides)

        taxi_feedback[taxi_id] = average_feedback

    # Find best taxi
    best_taxi = max(taxi_feedback, key=taxi_feedback.get)

    return best_taxi, taxi_feedback[best_taxi]


def determine_average_feedback_after_certain_time(ride_end_hour=22) -> float:
    # Determine the average feedback after given hour over all rides given by returned by function below
    # E.g. passing 'ride_end_hour=22' should return average feedback for rides after 22:00

    rides = get_all_rides()

    # Possible solution
    rides_after_hour = [ride for ride in rides if _ride_ended_after_given_hour(ride, ride_end_hour)]

    if len(rides_after_hour) <= 0:
        return 0.0

    average_feedback = sum([ride["feedbackAmountOfStars"] for ride in rides_after_hour]) / len(rides_after_hour)

    return average_feedback


def _ride_ended_after_given_hour(ride, hour):
    ride_end_datetime_obj = datetime.datetime.fromtimestamp(ride["rideEnd"] / 1000)

    return ride_end_datetime_obj.hour > hour
