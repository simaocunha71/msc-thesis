```
def check_monthnumber_number(month_number):
    if month_number in [1,3,5,7,8,10,12]:
        return False
    else:
        return True
```


The function `check_monthnumber_number` takes an integer as input which represents a month number. It checks if the month has 30 days or not. If the month is January, March, May, July, August, October, or December (which all have 31 days), the function returns `False`. Otherwise, it returns `True`.

This function passes the given unit test `assert check_monthnumber_number(6)==True`. For example, June (which is the 6th month) has 30 days, so the function returns `True`. Similarly, for other months with 30 days like April, September, November, and February (leap year), the function also returns `True`. For months with 31 days, the function returns `False`. 





Please note that this function does not consider leap years. For a more accurate solution, you would need to consider leap years and the fact that February can have either 28 or 29 days. 

Here is the more accurate function:

```
def check_monthnumber_number(month_number):
    if month_number in [4,6,9,11]:
        return True
    elif month_number == 2:
        return True
    else:
        return False
```

This function returns `True` for months with 30 days (April, June, September, November) and for February in a leap year. Otherwise, it returns `False`. 