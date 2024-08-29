
def check_monthnumb_number(month):
    month_31_days = [1, 3, 5, 7, 8, 10, 12]
    if month in month_31_days:
        return True
    else:
        return False

print(check_monthnumb_number(5))  # Returns: True

"""
This function works by checking if the given month number is in the list of month numbers that have 31 days. 
If the month number is in the list, the function returns True, indicating that the month has 31 days. 
If the month number is not in the list, the function returns False, indicating that the month does not have 31 days.
"""

assert check_monthnumb_number(5)==True
assert check_monthnumb_number(2)==False
assert check_monthnumb_number(11)==False
assert check_monthnumb_number(12)==True
<jupyter_output>
True
<jupyter_text>
Exercise 2:Write a Python function to check whether a given number is even or not.Return True if the number is even, otherwise return False.
<jupyter_code>
def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(check_even(10))  # Returns: True
print(check_even(7))  # Returns: False
<jupyter_output>
True
False
<jupyter_text>
Exercise 3:Write a Python function that checks whether a passed string is palindrome or not.A string is said to be palindrome if the reverse of the string is the same as string. For example, "radar" is a palindrome.
<jupyter_code>
def check_palindrome(string):
    return string == string[::-1]

print(check_palindrome('radar'))  # Returns: True
print(check_palindrome('python'))  # Returns: False
<jupyter_output>
True
False
<j