```
import datetime

def valid_date(date):
    # Split the date string into month, day, year
    month, day, year = date.split('-')

    # Convert the date string into datetime object
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        return False

    return True
```

Explanation:
The given function `valid_date` takes a date string as input and checks if it is valid according to the given rules. If the date string is valid, it returns True; otherwise, it returns False.

First, it splits the date string into month, day, and year. Then, it tries to convert this date string into a datetime object using the `datetime.datetime` function. If the conversion is successful, it means the date is valid. If the conversion raises a `ValueError`, it means the date is invalid.

Note that the `datetime.datetime` function will raise a `ValueError` if the date is not in the correct format (mm-dd-yyyy) or if the values of month, day, or year are not valid. This is exactly what we want, as it allows us to catch invalid dates and return False. If the date is valid, the function will return True.