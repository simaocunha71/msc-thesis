
def last_Digit(n):
    return n % 10

print(last_Digit(123))

# Alternate Solution 

def last_Digit(n):
    return int(str(n)[-1])

print(last_Digit(123))

# Explanation:
# 1. In the first function, we use the modulus operator to find the remainder of the division of the number by 10. This gives us the last digit of the number.
# 2. In the second function, we convert the number to a string, get the last character of the string (which is the last digit) and convert it back to an integer.

# Both these functions will give the same output for the given example.

# Output:
# 3
# 3
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:Write a Python function to find out whether a given number is a palindrome or not. A palindrome is a number that remains the same when its digits are reversed. For example, 121, 12321, 1001 etc.
<jupyter_code>
# Solution:

def is_Palindrome(n):
    return str(n) == str(n)[::-1]

print(is_Palindrome(121))
print(is_Palindrome(12321))
print(is_Palindrome(1001))

# Explanation:
# The function converts the number to a string, and then checks if the string is equal to its reverse. If it is, the function returns True, indicating that the number is a palindrome. If not, it returns False.

# Output:
# True
# True
# True
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3:Write a Python function that takes in a list of integers and returns the sum of all the even numbers in the list.
<jupyter_code>
# Solution:

def sum_Even(lst):
