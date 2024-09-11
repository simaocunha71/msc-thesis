def check_monthnumber_number(month):
    if month == 2:
        return False
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return False
    else:
        return True

# Testing the function
print(check_monthnumber_number(6))



"""
Correct Solution:
"""
def check_monthnumber_number(month):
    months = [1, 3, 5, 7, 8, 10, 12]
    return month not in months

# Testing the function
print(check_monthnumber_number(6))  # True

```
    
```
"""
Write a function to check whether the given month number contains 30 days or not. Months are given as number from 1 to 12.
assert check_monthnumber_number(6)==True
"""

def check_monthnumber_number(month):
    if month == 2:
        return False
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return False
    else:
        return True
```
```

```
"""
Write a function to check whether the given month number contains 30 days or not. Months are given as number from 1 to 12.
assert check_monthnumber_number(6)==True
"""

def check_monthnumber_number(month):
    months = [1, 3, 5, 7, 8, 10, 12]
    return month not in months

# Testing the function
print(check_monthnumber_number(6))  # True
```

```python
"""
Write a function to check whether the given month number contains 30 days or not. Months are given as number from 1 to 12.
assert check_monthnumber_number(6)==True
"""

def check_monthnumber_number(month):
    if month == 2:
        return False
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return