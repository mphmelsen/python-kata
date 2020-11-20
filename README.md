# Python coding exercise

**Prerequisites:**
- Python 3.7

## Given
- An imaginary DynamoDB table
- With item attributes:
  - `companyId`
  - `taxiId`
  - `rideId`
  - `rideDuration`
  - `rideStart`
  - `rideEnd`
  - `feedbackAmountOfStars`

The response you'd normally get from querying the DynamoDB table are implemented in functions in `src/imaginary_dynamodb_table.py`.

# Exercise
* Implement functions in `src/main.py`. The functions contain a doc statement what they're supposed to do.
  * Utilize `test/test_main.py` to add unit tests
* If time allows, annotate the functions with static types from `typing` lib.
