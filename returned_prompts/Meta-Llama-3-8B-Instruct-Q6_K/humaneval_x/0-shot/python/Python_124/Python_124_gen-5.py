```
def valid_date(date):
    # Split the date by '-' and check if it has 3 parts
    if '-' not in date:
        return False
    date_parts = date.split('-')
    if len(date_parts) != 3:
        return False

    month, day, year = date_parts
    month = int(month)
    day = int(day)
    year = int(year)

    # Check if the month is between 1 and 12
    if month < 1 or month > 12:
        return False

    # Check if the day is valid for the given month
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
```


In this solution, we first split the date string by the '-' character to get the month, day, and year. We then check if the month is between 1 and 12, and if the day is valid for the given month. We use a list of month indices to check if the month is a month with 31 days, 30 days, or 29 days (for February, which has 29 days in leap years). If any of these checks fail, we return False. If all checks pass, we return True.