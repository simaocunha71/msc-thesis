```
def check_monthnumb_number(month_num):
    if month_num in [1, 3, 5, 7, 8, 10, 12]:
        return True
    else:
        return False
```

The function `check_monthnumb_number` takes an integer as an argument, which represents the month number. The function checks if the month number is in the list of months that have 31 days (January, March, May, July, August, October, and December). If the month number is in the list, the function returns `True`, indicating that the month has 31 days. If the month number is not in the list, the function returns `False`, indicating that the month does not have 31 days. The unit test `assert check_monthnumb_number(5)==True` verifies the function's correctness by checking that May (which has 31 days) returns `True`. 





