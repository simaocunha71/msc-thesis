```
def check_monthnumb_number(month_num):
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    return month_num in months_with_31_days
```


In this solution, we define a list `months_with_31_days` that contains the month numbers that have 31 days. Then, we use the `in` operator to check if the given month number is in this list. If it is, we return `True`, indicating that the month has 31 days. Otherwise, we return `False`. The unit test `assert check_monthnumb_number(5)==True` ensures that the function correctly identifies month 5 as having 31 days.