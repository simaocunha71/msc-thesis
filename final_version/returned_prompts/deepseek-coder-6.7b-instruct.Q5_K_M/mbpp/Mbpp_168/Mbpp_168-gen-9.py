
def frequency(lst, n):
    return lst.count(n)

print(frequency([1,2,3], 4))  # 0

"""
Write a function to count the number of occurrences of a number in a given list.
assert frequency([1,2,3,2,2,4,2,5,2,6,2], 2) == 5
"""

def frequency(lst, n):
    return lst.count(n)

print(frequency([1,2,3,2,2,4,2,5,2,6,2], 2))  # 5

"""
Write a function to count the number of occurrences of a number in a given list.
assert frequency([1,1,1,1], 1) == 4
"""

def frequency(lst, n):
    return lst.count(n)

print(frequency([1,1,1,1], 1))  # 4
<jupyter_output>
0
5
4
<jupyter_text>
6. Write a function to check if a given string is a palindrome.
<jupyter_code>
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome('madam'))  # True
print(is_palindrome('hello'))  # False
<jupyter_output>
True
False
<jupyter_text>
7. Write a function to reverse a string.
<jupyter_code>
def reverse_string(s):
    return s[::-1]

print(reverse_string('hello'))  # 'olleh'
print(reverse_string('world'))  # 'dlrow'
<jupyter_output>
olleh
dlrow
<jupyter_text>
8. Write a function to find the factorial of a number.
<jupyter_code>
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
