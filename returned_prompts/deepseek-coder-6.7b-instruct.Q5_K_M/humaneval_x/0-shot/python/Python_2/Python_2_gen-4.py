
    return number % 1

# Tests:
print(truncate_number(3.5))  # 0.5
print(truncate_number(12.87))  # 0.87
print(truncate_number(0.2345))  # 0.2345
print(truncate_number(10.0))  # 0.0
print(truncate_number(7))  # 0.0


'''
The modulus operator (%) gives the remainder of the division of the number by 1. 
By using this operator, we can isolate and return the decimal part of the number.
'''

# This function is applicable for positive floating point numbers,
# and will return 0.0 for integers as there are no decimals in the integer part.
<jupyter_output>
0.5
0.87
0.2345
0.0
0.0
<jupyter_text>
Task 2: Palindrome CheckerCreate a function that checks whether a given string is a palindrome or not.
<jupyter_code>
