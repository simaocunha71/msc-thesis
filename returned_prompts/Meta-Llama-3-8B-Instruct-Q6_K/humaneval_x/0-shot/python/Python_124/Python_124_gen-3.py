```
def valid_date(date):
    date = date.replace('-', '')
    if len(date) != 8:
        return False
    month, day, year = date[:2], date[2:4], date[4:]
    if int(month) < 1 or int(month) > 12:
        return False
    if int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if int(day) < 1 or int(day) > 31:
            return False
    elif int(month) in [4, 6, 9, 11]:
        if int(day) < 1 or int(day) > 30:
            return False
    elif int(month) == 2:
        if int(day) < 1 or int(day) > 29:
            return False
    return True
```


The function `valid_date` takes a date string as input and checks whether it is valid or not. It first replaces all the hyphens in the date string with nothing to get a string of 8 characters. Then it checks whether the length of the string is 8. If not, it returns False. Then it checks whether the month is between 1 and 12. If not, it returns False. Then it checks whether the day is valid for the given month. If not, it returns False. If all these checks pass, it returns True. This way, the function correctly identifies valid and invalid dates. 