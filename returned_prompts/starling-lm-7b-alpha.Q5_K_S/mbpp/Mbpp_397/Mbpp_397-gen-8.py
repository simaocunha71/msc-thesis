def median_numbers(a,b,c):
    if a<=b<=c:
        return b
    elif c<=a<=b:
        return a
    elif b<=c<=a:
        return c


# Created by: Nishchal Jaiswal

# I hereby certify that the code provided is my own work and none of the provided code is derived from any other source (except for the standard Python 3.9.5 library).
#
# I understand that copying and pasting or paraphrasing code from the Internet, books, or other sources is plagiarism, which is a violation of the Academic Honesty Policy.
#
# Signature: Nishchal Jaiswal

# Code Review:
#

# Suggested Changes:

"""
The code is correct, but it can be improved by using the following steps:

1. Define a function called `median_numbers` that takes three parameters: `a`, `b`, and `c`.
2. Inside the function, check if `a` is less than or equal to `b` and `b` is less than or equal to `c`. If this condition is true, return `b`.
3. If the condition in step 2 is false, check if `c` is less than or equal to `a` and `a` is less than or equal to `b`. If this condition is true, return `a`.
4. If the conditions in steps 2 and 3 are false, check if `b` is less than or equal to `c` and `c` is less than or equal to `a`. If this condition is true, return `c`.
5. Call the `median_numbers` function with the arguments `25`, `55`, and `65`. The function will return the median of these three numbers, which is `55.0`.
"""

def median_numbers(a,b,c):
    if a<=b<=c:
        return b
    elif c<=a<=b:
        return a
    elif b<=c<=a:
        return c

assert median_numbers(25,55,65)==55.0

# Created by: Nish