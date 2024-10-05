```
def valid_date(date):
    date = date.split('-')
    month, day, year = int(date[0]), int(date[1]), int(date[2])
    if month < 1 or month > 12:
        return False
    if day < 1:
        return False
    if (month == 2 and day > 29) or (month in [1, 3, 5, 7, 8, 10, 12] and day > 31) or (month in [4, 6, 9, 11] and day > 30):
        return False
    return True
```


Solution:
The task is to create a function that validates a given date string and returns True if the date is valid, otherwise False. The date is valid if it follows the rules:

1. The date string is not empty.
2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
3. The months should not be less than 1 or higher than 12.
4. The date should be in the format: mm-dd-yyyy.

Here is a Python function that solves this problem:

```
def valid_date(date):
    date = date.split('-')
    month, day, year = int(date[0]), int(date[1]), int(date[2])
    if month < 1 or month > 12:
        return False
    if day < 1:
        return False
    if (month == 2 and day > 29) or (month in [1, 3, 5, 7, 8, 10, 12] and day > 31) or (month in [4, 6, 9, 11] and day > 30):
        return False
    return True
```

This function first splits the date string into month, day, and year. Then it checks if the month is between 1 and 12, and if the day is between 1 and 31. If the month is February, it also checks if the day is between 1 and 29.