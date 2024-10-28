
```python
def valid_date(date):
    if date == '':
        return False
    date_parts = date.split('-')
    if len(date_parts) != 3:
        return False
    month, day, year = date_parts
    try:
        month, day, year = int(month), int(day), int(year)
    except:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2:
        if day > 29:
            return False
        elif day == 29 and not (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
            return False
    return True
```

This Python function validates a given date string by checking each of the rules specified in the problem. It first checks if the date string is not empty and if it is in the correct format (mm-dd-yyyy). It then converts the month, day, and year parts to integers. It checks if the month is between 1 and 12, the day is between 1 and 31, and the day is valid for the given month. If all checks pass, the function returns True; otherwise, it returns False.
