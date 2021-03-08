import datetime

from src.imaginary_dynamodb_table import get_all_rides


def determine_average_ride_duration_minute_per_taxi():
    # Determine the average ride duration in minutes per taxi given the rides returned by 'get_all_rides' function below
    # Expected return format:
    # {
    #     <taxiId>: <averageRunDurationMinutesRoundedOff>,
    #     ...
    # }

    rides = get_all_rides()
    totals = {}
    for ride in rides:
        duration = ride['rideEnd'] - ride['rideStart']
        try:
            totals[ride['taxiId']]['duration'] += duration
            totals[ride['taxiId']]['number'] += 1
        except KeyError:
            totals[ride['taxiId']] = {'duration': duration, 'number': 1}

    averages = {}
    for taxi, values in totals.items():
        averages[taxi] = float("{:.1f}".format((values['duration']/values['number'])/60000))
    print(averages)
    return averages


def determine_taxi_with_best_feedback():
    # Determine the taxi that got the best feedback given the rides returned by 'get_all_rides' function below
    # Expected return format:
    # <taxiId>, <averageFeedback>

    rides = get_all_rides()
    best_score = 0
    best_taxi = 0
    for ride in rides:
        taxi = ride['taxiId']
        feedback = ride['feedbackAmountOfStars']
        if feedback > best_score:
            best_score = feedback
            best_taxi = taxi
    print(f'{best_taxi}, {best_score}')
    return best_taxi, best_score


def determine_average_feedback_after_certain_time(ride_end_hour=22):
    # Determine the average feedback after given hour over all rides returned by the 'get_all_rides' function below
    # E.g. passing 'ride_end_hour=22' should return average feedback for rides after 22:00

    rides = get_all_rides()
    totals = 0
    ride_nr = 0
    for ride in rides:
        end_epoch = ride['rideEnd'] / 1000.0
        end_time = datetime.datetime.fromtimestamp(end_epoch)
        if end_time.hour < ride_end_hour:
            continue
        feedback = ride['feedbackAmountOfStars']
        totals += feedback
        ride_nr += 1
    if totals == 0:
        return None
    average = float('{:.1f}'.format(totals/ride_nr))
    print(average)
    return average


if __name__ == '__main__':
    determine_average_ride_duration_minute_per_taxi()
    determine_taxi_with_best_feedback()
    determine_average_feedback_after_certain_time()
