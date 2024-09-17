```
def check_monthnumber_number(month_number):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return months[month_number-1] == 30
```



Explanation:
The problem is asking to write a function that checks whether a given month number contains 30 days or not. 

The months are given as a number from 1 to 12, so we can create a list of the number of days in each month. 

The function takes the month number as an input, subtracts 1 from it to match the list index, and then checks if the number of days in that month is 30. 

The unit test `assert check_monthnumber_number(6)==True` helps in understanding that the function should return `True` for the month 6, which has 30 days. 

The function `check_monthnumber_number` is defined to solve the problem. It takes the month number as an argument, subtracts 1 from it to match the list index, and then checks if the number of days in that month is 30. If it is, the function returns `True`; otherwise, it returns `False`. 





