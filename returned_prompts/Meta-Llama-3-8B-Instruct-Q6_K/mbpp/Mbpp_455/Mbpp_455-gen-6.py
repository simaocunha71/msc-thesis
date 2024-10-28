```
def check_monthnumb_number(month_number):
    if 1<=month_number<=12:
        if month_number in [1,3,5,7,8,10,12]:
            return True
        else:
            return False
    else:
        return "Invalid month number"
```


Explanation: 
The problem is asking to create a function that takes a month number as input and returns True if the month contains 31 days, otherwise returns False. 

The function first checks if the month number is within the range of 1 to 12 (inclusive). If the number is not within this range, it returns an error message. 

If the month number is valid, it checks if the month is January, March, May, July, August, October, or December, which are the months that have 31 days. If the month is one of these, the function returns True. If the month is not one of these, the function returns False. 

The unit test `assert check_monthnumb_number(5)==True` helps to clarify the problem by showing that the function should return True for the month number 5, which is May and has 31 days. 

The function can be used to check the number of days in any month, by passing the month number as an argument. For example, `check_monthnumb_number(1)` would return True for January, which has 31 days. 

However, please note that the problem does not specify what to do if the month number is invalid (i.e., not in the range 1-12). In this solution, I have chosen to return an error message in such cases. You could modify the function to handle invalid month numbers in a different way if needed. 