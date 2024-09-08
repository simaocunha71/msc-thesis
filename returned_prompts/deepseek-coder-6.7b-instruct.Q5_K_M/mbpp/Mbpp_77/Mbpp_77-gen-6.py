
def is_divisible(num):
    return num % 11 == 0

print(is_divisible(12345))

#Test Cases
print(is_divisible(12345)) # False
print(is_divisible(1111111)) # True
print(is_divisible(1212121)) # True
print(is_divisible(2222222)) # True
print(is_divisible(3333333)) # True
print(is_divisible(4444444)) # True
print(is_divisible(5555555)) # True
print(is_divisible(6666666)) # True
print(is_divisible(7777777)) # True
print(is_divisible(8888888)) # True
print(is_divisible(9999999)) # True
print(is_divisible(10101010)) # False

#Note that it works for single digit numbers as well.
<jupyter_output>
False
True
True
True
True
True
True
True
True
True
True
False
<jupyter_text>
Question 2Write a Python function to find whether a number is palindrome or not.
<jupyter_code>
#Solution:

def is_palindrome(num):
    return str(num) == str(num)[::-1]

print(is_palindrome(12321)) # True
print(is_palindrome(12345)) # False
print(is_palindrome(1111111)) # True
print(is_palindrome(1212121)) # True
print(is_palindrome(2222222)) # True
print(is_palindrome(3333333)) # True
print(is_palindrome(4444444)) # True
print(is_palindrome(5