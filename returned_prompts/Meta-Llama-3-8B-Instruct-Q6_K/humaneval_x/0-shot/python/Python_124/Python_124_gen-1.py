```
def valid_date(date):
    date = date.replace('-', '')
    if len(date) != 8:
        return False
    month, day, year = int(date[:2]), int(date[2:4]), int(date[4:])
    if month < 1 or month > 12:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month == 2:
        if day < 1 or day > 29:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    return True
```


# Test Cases:
print(valid_date('03-11-2000'))  # Expected Output: True
print(valid_date('15-01-2012'))  # Expected Output: False
print(valid_date('04-0-2040'))  # Expected Output: False
print(valid_date('06-04-2020'))  # Expected Output: True
print(valid_date('06/04/2020'))  # Expected Output: False
```


# Explanation:
The function takes a date string as input and returns True if the date is valid and False otherwise. The date string should be in the format "mm-dd-yyyy". The function checks the following conditions:
1. The date string should not be empty.
2. The number of days should not be less than 1 or higher than 31 for months 1,3,5,7,8,10,12.
3. The number of days should not be less than 1 or higher than 30 for months 4,6,9,11.
4. The number of days should not be less than 1 or higher than 29 for the month 2.
5. The month should not be less than 1 or higher than 12.
6. The date should be in the format "mm-dd-yyyy".

If all the conditions are satisfied, the function returns True; otherwise, it returns False. The function uses the `replace` method to remove the hyphens from the date string and then checks the conditions using if-else statements. The function returns True if the date is valid and False otherwise.