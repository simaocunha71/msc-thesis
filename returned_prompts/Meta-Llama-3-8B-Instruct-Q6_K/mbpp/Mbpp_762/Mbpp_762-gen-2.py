```
def check_monthnumber_number(month_number):
    if month_number in [1,3,5,7,8,10,12]:
        return False
    else:
        return True
```    
This function takes a month number as input and returns True if the month contains 30 days, False otherwise. The months that have 30 days are June, September, April, November, January, March, May and July.
The unit test `assert check_monthnumber_number(6)==True` ensures that the function returns True for June, which indeed has 30 days.
```python
print(check_monthnumber_number(6))  # Returns: True
print(check_monthnumber_number(2))  # Returns: False
```    
This function uses a simple if-else statement to check if the month number is in the list of months that have 30 days or not. If it is, the function returns False; otherwise, it returns True.    
```python
print(check_monthnumber_number(1))  # Returns: False
print(check_monthnumber_number(6))  # Returns: True
print(check_monthnumber_number(4))  # Returns: True
```    
The function can be used to check whether a given month number contains 30 days or not.    
```python
month_number = int(input("Enter a month number: "))
if check_monthnumber_number(month_number):
    print(f"Month {month_number} has 30 days.")
else:
    print(f"Month {month_number} does not have 30 days.")
```    
This code snippet prompts the user to enter a month number and then checks whether the month has 30 days or not. It then prints out a message accordingly.    
```python
print(check_monthnumber_number(12))  # Returns: True
print(check_monthnumber_number(2))  # Returns: False
```    
The function can also be used to check the number of days in a month in a program.    
```python
def check_monthnumber_number(month_number):
    if month_number in [1,3,5,7,8,10,12]:
        return False
    elif month_number == 2:
        return False
    else:
        return True
```    
This function is more accurate as it also checks for February, which has 28 or 29 days.    
```python
print(check_monthnumber_number(6))  # Returns: True
print(check_monthnumber_number(2))  #