```
def check_monthnumb_number(month_num):
    if month_num in [1, 3, 5, 7, 8, 10, 12]:
        return True
    else:
        return False
```
The function takes a month number as an argument and checks whether it is a month with 31 days or not. It returns True if the month has 31 days and False otherwise.

The unit test `assert check_monthnumb_number(5)==True` suggests that the function should return True for the month number 5 (May), which indeed has 31 days. The function passes this test. 

The function uses a conditional statement to check if the month number is in the list of months with 31 days. If the month number is in the list, the function returns True; otherwise, it returns False. The list includes the months January, March, May, July, August, October, and December, which are the months with 31 days. 

This function does not consider leap years, so it will return False for February, even if it is a leap year. If you need to consider leap years, you would need to add additional logic to the function. 