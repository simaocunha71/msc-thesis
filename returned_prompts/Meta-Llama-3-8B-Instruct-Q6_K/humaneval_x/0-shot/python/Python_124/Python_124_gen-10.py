```
def valid_date(date):
    parts = date.split('-')
    if len(parts) != 3:
        return False
    month, day, year = map(int, parts)
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
```


This function splits the date string into three parts: month, day, and year. It then checks each part to ensure it meets the given conditions. If any part fails to meet the conditions, the function returns False. If all parts meet the conditions, the function returns True. The function uses a list comprehension to convert the parts to integers. It also uses conditional statements to check the month and day. The function returns True if the date is valid and False otherwise.