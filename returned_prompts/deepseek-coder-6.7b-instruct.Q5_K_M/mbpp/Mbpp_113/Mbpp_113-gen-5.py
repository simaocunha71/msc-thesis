def check_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
"""
Test the function:
"""
print(check_integer("python")) # False
print(check_integer("123")) # True
<jupyter_output>
False
True
<jupyter_text>
3. Write a Python function to check whether a string is a palindrome or not. (A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization).
<jupyter_code>
def check_palindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    return s == s[::-1]
"""
Test the function:
"""
print(check_palindrome("A man, a plan, a canal: Panama")) # True
print(check_palindrome("Python")) # False
<jupyter_output>
True
False
<jupyter_text>
4. Write a function to calculate the factorial of a number (a non-negative integer). The function should accept the number as an argument.
<jupyter_code>
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
"""
Test the function:
"""
print(factorial(5)) # 120
print(factorial(0)) # 1
<jupyter_output>
120
1
<jupyter_text>
5. Write a function that returns the count of characters in a string.
<jupyter_code>
def count_characters(s):
    return len(s)
"""
Test the function:
"""
print(count_characters("hello")) # 5
print(count_characters("world")) # 5
<jupyter_output>
5
5
<jupyter_text>
6. Write a Python function to reverse a string.
<jup