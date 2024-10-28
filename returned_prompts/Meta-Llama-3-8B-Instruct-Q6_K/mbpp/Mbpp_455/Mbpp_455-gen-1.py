```
def check_monthnumb_number(month_number):
    if month_number in [1,3,5,7,8,10,12]:
        return True
    else:
        return False
```



Note: In this problem, we are given a month number, and we need to check whether this month contains 31 days or not. 

The given unit test `assert check_monthnumb_number(5)==True` suggests that we need to check whether the month number is in the list of months that have 31 days. 

So, the function `check_monthnumb_number` checks if the given month number is in the list of months that have 31 days. If it is, the function returns `True`, otherwise it returns `False`. 

The list of months that have 31 days is [1,3,5,7,8,10,12]. This list includes all the months except February which has 28 or 29 days depending on whether it is a leap year or not. 

Here is the Python function that solves the problem:

```
def check_monthnumb_number(month_number):
    if month_number in [1,3,5,7,8,10,12]:
        return True
    else:
        return False
```



This function works by checking if the given month number is in the list of months that have 31 days. If it is, the function returns `True`, otherwise it returns `False`. This function passes the given unit test. 