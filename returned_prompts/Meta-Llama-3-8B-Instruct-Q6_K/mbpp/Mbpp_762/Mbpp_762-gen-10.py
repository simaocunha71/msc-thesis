```
def check_monthnumber_number(month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return False
    else:
        return True
```    
The function `check_monthnumber_number` takes a month number as input and returns `True` if the month has 30 days, and `False` otherwise. The function uses a list comprehension to check if the month is in the list of months that do not have 30 days. If the month is not in the list, the function returns `True`, indicating that the month has 30 days. If the month is in the list, the function returns `False`, indicating that the month does not have 30 days. The unit test `assert check_monthnumber_number(6)==True` shows that the function should return `True` for the month of June, which has 30 days.