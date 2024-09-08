def lateralsuface_cylinder(r,h):
    return 2*3.141592653589793*r*h

# Test Cases:
print(lateralsuface_cylinder(10,5))

# Expected Output:
# 314.15000000000003
<jupyter_output>
314.1592653589793
<jupyter_text>
Problem 4: Given a string s, write a function to return the number of vowels in the string.
<jupyter_code>
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Test Cases:
print(count_vowels("Hello, World!"))

# Expected Output:
# 3
<jupyter_output>
3
<jupyter_text>
Problem 5: Write a function to check if a given string is a palindrome.
<jupyter_code>
def is_palindrome(s):
    return s == s[::-1]

# Test Cases:
print(is_palindrome("radar"))
print(is_palindrome("hello"))

# Expected Outputs:
# True
# False
<jupyter_output>
True
False
<jupyter_text>
Problem 6: Write a function to return the factorial of a number.
<jupyter_code>
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test Cases:
print(factorial(5))
print(factorial(0))

# Expected Outputs:
# 120
# 1
<jupyter_output>
120
1
<jupyter_text>
