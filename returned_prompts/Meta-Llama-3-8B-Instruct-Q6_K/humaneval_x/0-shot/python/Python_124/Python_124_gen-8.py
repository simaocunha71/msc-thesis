```
def valid_date(date):
    try:
        month, day, year = map(int, date.split('-'))
        if month < 1 or month > 12:
            return False
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day < 1 or day > 31:
                return False
        elif month in [4, 6, 9, 11]:
            if day < 1 or day > 30:
                return False
        elif month == 2:
            if day < 1 or day > 29:
                return False
        return True
    except ValueError:
        return False
```


Explanation:

The function `valid_date(date)` takes a date string as input and returns `True` if the date is valid according to the given rules and `False` otherwise.

First, it splits the date string into three parts using the '-' character as the separator, converts each part to an integer, and assigns it to the `month`, `day`, and `year` variables.

Then, it checks if the `month` is within the range 1 to 12. If not, it returns `False`.

Next, it checks the validity of the `day` based on the `month`. For months 1, 3, 5, 7, 8, 10, and 12, it checks if the `day` is within the range 1 to 31. For months 4, 6, 9, and 11, it checks if the `day` is within the range 1 to 30. For month 2, it checks if the `day` is within the range 1 to 29.

If any of these checks fail, the function returns `False`.

If all the checks pass, the function returns `True`.

The `try`-`except` block is used to catch any `ValueError` that might occur when trying to convert the date string to integers. If a `ValueError` occurs, the function returns `False`. This is to handle cases where the input date string is not in the correct format. For example, if the input date string is '06/04/2020' instead of '06-04-2020', the function will return `False`.