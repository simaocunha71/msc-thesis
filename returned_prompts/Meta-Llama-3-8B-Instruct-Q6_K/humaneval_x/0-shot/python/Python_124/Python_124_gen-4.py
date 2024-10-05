```
def valid_date(date):
    date_format = "%m-%d-%Y"
    try:
        datetime.datetime.strptime(date, date_format)
        month, day, year = map(int, date.split('-'))
        if month < 1 or month > 12:
            return False
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day < 1 or day > 31:
                return False
        elif month == 2:
            if day < 1 or day > 29:
                return False
        elif month in [4, 6, 9, 11]:
            if day < 1 or day > 30:
                return False
        return True
    except ValueError:
        return False
```


This function `valid_date` takes a date string as input, checks if the date is in the correct format and if the date is valid according to the given rules. It returns `True` if the date is valid and `False` otherwise.

The function first tries to parse the date string using `strptime` method from `datetime` module. If the parsing is successful, it means the date is in the correct format. Then it extracts the month, day and year from the date string.

It then checks if the month is within the range 1 to 12. If not, it returns `False`.

Next, it checks the number of days in the month. If the month is one of the months with 31 days (January, March, May, July, August, October, December), it checks if the day is within the range 1 to 31. If not, it returns `False`. If the month is February, it checks if the day is within the range 1 to 29 (29 for leap years). If not, it returns `False`. If the month is one of the months with 30 days (April, June, September, November), it checks if the day is within the range 1 to 30. If not, it returns `False`.

If all the checks pass, it returns `True`, meaning the date is valid. If any of the checks fail, it returns `False`, meaning the date is invalid. If the date string is not in the correct format, `strptime` method will raise a `ValueError` exception, which is caught and `False` is returned.