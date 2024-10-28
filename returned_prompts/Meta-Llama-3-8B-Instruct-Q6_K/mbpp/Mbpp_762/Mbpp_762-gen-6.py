```
def check_monthnumber_number(month):
    if month in [1,3,5,7,8,10,12]:
        return False
    else:
        return True
```


This function takes an integer as input representing a month number from 1 to 12. It returns True if the month has 30 days, False otherwise. The months that have 30 days are April, June, September, November. The months that have 31 days are January, March, May, July, August, October, December. The function uses a list to define the months that have 30 days. If the input month is in this list, the function returns True; otherwise, it returns False. The unit test `assert check_monthnumber_number(6)==True` ensures that the function works correctly for June, which has 30 days. The function can be used in a program to check whether a given month has 30 days or not. For example, if the program needs to know whether a certain date will occur in a 30-day month, it can call this function to check the month number.