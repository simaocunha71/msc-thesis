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
            if year % 4 != 0:
                if day < 1 or day > 28:
                    return False
            else:
                if day < 1 or day > 29:
                    return False
        return True
    except ValueError:
        return False
```


Here is the explanation of the code:

1. We first try to split the date string by the '-' character and convert each part to an integer. If this fails, we return False because the date is not in the correct format.

2. We then check if the month is less than 1 or greater than 12. If it is, we return False because the month is not valid.

3. We then check the number of days for each month. If the month is one of the months with 31 days (January, March, May, July, August, October, December), we check if the day is less than 1 or greater than 31. If it is, we return False. Similarly, if the month is one of the months with 30 days (April, June, September, November), we check if the day is less than 1 or greater than 30. If it is, we return False.

4. For the month of February, we have to take into account leap years. If the year is not a leap year, we check if the day is less than 1 or greater than 28. If it is, we return False. If the year is a leap year, we check if the day is less than 1 or greater than 29. If it is, we return False.

5. If we have not returned False by this point, we return True because the date is valid.

6. If the code reaches the end of the function without returning False, it means that the date is valid, so we return True. If a ValueError is raised during the execution of the function