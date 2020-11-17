import random
from uuid import uuid4


def get_all_rides():
    start_time = 1577836800000  # 1st of January 2020
    end_time = 1609372800000  # 31st of December 2020

    rides = []
    for _ in range(0, random.randint(50, 250)):
        ride_start = random.randint(start_time, end_time)
        ride_end = ride_start + random.randint(5 * 60 * 1000, 5 * 60 * 60 * 1000)  # Ride duration between 5 min - 5 hr

        rides.append(
            {
                "companyId": random.randint(1, 4),
                "taxiId": random.randint(1000, 1010),
                "rideId": str(uuid4()),
                "rideStart": ride_start,
                "rideEnd": ride_end,
                "feedbackAmountOfStars": random.randint(0, 5)
            }
        )

    return iter(rides)


if __name__ == '__main__':
    print(list(get_all_rides()))
