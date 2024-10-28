```
def check_monthnumb_number(month_number):
    if (month_number == 1 or month_number == 3 or month_number == 5 or month_number == 7 or month_number == 8 or month_number == 10 or month_number == 12):
        return True
    else:
        return False
```

The function `check_monthnumb_number` takes an integer as input which represents the month number. It checks if the month number is 1, 3, 5, 7, 8, 10, or 12. If it is, the function returns `True`, indicating that the month has 31 days. Otherwise, it returns `False`. This function is designed to work with the Gregorian calendar, which is the most commonly used calendar in the world. The unit test `assert check_monthnumb_number(5)==True` ensures that the function works correctly for the month of May, which has 31 days. 





