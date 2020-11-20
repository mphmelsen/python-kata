from src.imaginary_dynamodb_table import get_all_rides


def determine_average_ride_duration_minute_per_taxi():
    # Determine the average ride duration in minutes per taxi given the rides returned by 'get_all_rides' function below
    # Expected return format:
    # {
    #     <taxiId>: <averageRunDurationMinutesRoundedOff>,
    #     ...
    # }

    rides = get_all_rides()

    pass


def determine_taxi_with_best_feedback():
    # Determine the taxi that got the best feedback given the rides returned by 'get_all_rides' function below
    # Expected return format:
    # <taxiId>, <averageFeedback>

    rides = get_all_rides()

    pass


def determine_average_feedback_after_certain_time(ride_end_hour=22):
    # Determine the average feedback after given hour over all rides returned by the 'get_all_rides' function below
    # E.g. passing 'ride_end_hour=22' should return average feedback for rides after 22:00

    rides = get_all_rides()

    pass


if __name__ == '__main__':
    determine_average_ride_duration_minute_per_taxi()
    determine_taxi_with_best_feedback()
    determine_average_feedback_after_certain_time()
