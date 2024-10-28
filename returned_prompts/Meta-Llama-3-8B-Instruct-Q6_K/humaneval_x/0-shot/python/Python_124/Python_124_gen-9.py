```
def valid_date(date):
    date = date.replace('-', '')
    if len(date) != 8:
        return False
    if date[2] != '-':
        return False
    month, day, year = date.split('-')
    if int(month) < 1 or int(month) > 12:
        return False
    if int(day) < 1 or int(day) > 31:
        return False
    if int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if int(day) > 31:
            return False
    if int(month) == 2:
        if int(day) > 29:
            return False
    if int(month) in [4, 6, 9, 11]:
        if int(day) > 30:
            return False
    return True
``` 

```
This function first replaces the hyphens in the date string with empty strings. Then, it checks if the resulting string has a length of 8. If not, it returns False. Then, it checks if the second character is a hyphen. If not, it returns False. Then, it splits the date string into month, day, and year components. It checks if the month is less than 1 or greater than 12. If so, it returns False. It checks if the day is less than 1 or greater than 31. If so, it returns False. Then, it checks the month and day for specific rules. If the day is greater than the allowed number of days for the month, it returns False. Finally, it returns True if all checks pass. If any check fails, it returns False. 

Note: The function does not handle dates that have a leading zero in the month or day, such as '03-11-2000'. This is because the problem statement does not specify what to do with leading zeros. If leading zeros are intended to be allowed, the function would need to be modified to handle them. 

Also, the function does not handle dates that are not in the 'mm-dd-yyyy' format. If dates in other formats are intended to be allowed, the function would need to be modified to handle them. 

Finally, the function does not handle dates that are not valid for the specific year. For example, February 30, 2020 is not a valid date, but the function would return True for