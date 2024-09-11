```
def check_monthnumber_number(x):
    month_list = [4,6,9,11]
    if x in month_list:
        return True
    else:
        return False
```

Explanation:

This is a simple function that checks if the month number is in the month_list. If it is, it returns True, otherwise it returns False.

The month_list consists of all the months that contain 30 days, namely April, June, September, and November.

To test the function, you can use the assert statement to check if the function returns True when given the month number 6, which corresponds to June.

In this case, the function will return True because June is one of the months in the month_list that contains 30 days.

Overall, this function is a simple and straightforward way to determine if a given month number has 30 days or not.

Here are some additional tips for improving the function:

- Instead of using a list to store the months with 30 days, you can use a set to improve the lookup time for checking if a month number is in the list.

- You can also add error handling to the function to ensure that the month number is within the valid range of 1 to 12. This can be done using an if statement to check if the month number is greater than 12 or less than 1, and if so, raise an exception or return an error message.

- Additionally, you can use the built-in datetime module in Python to calculate the number of days in a month more accurately. This can be done using the `calendar.monthrange()` function from the calendar module, which returns a tuple containing the starting and ending weekday of the month, as well as the number of days in the month.

Overall, these tips can help improve the accuracy and reliability of the function, as well as make it more robust against invalid input.

```python
import calendar

def check_monthnumber_number(x):
    if x < 1 or x > 12:
        raise ValueError("Month number must be between 1 and 12")
    days_in_month = calendar.monthrange(2000, x)[1]
    if days