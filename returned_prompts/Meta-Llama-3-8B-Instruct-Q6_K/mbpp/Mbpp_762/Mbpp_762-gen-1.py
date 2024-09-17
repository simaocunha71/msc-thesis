```
def check_monthnumber_number(month_number):
    if month_number in [1, 3, 5, 7, 8, 10, 12]:
        return False
    else:
        return True
```



In this code, we define a function `check_monthnumber_number` that takes a month number as input. We then use a conditional statement to check if the month number is in the list of months that have 31 days (January, March, May, July, August, October, December). If the month number is in this list, the function returns `False`, indicating that the month does not have 30 days. Otherwise, it returns `True`, indicating that the month does have 30 days. The unit test `assert check_monthnumber_number(6)==True` is also included to verify that the function works correctly.