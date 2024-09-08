"""
Firstly, the catalan number is given by the formula:
C(n) = (2n choose n) / (n+1)

This formula can be implemented using the math library's combination function.

Here is a Python program that uses this formula to compute the nth catalan number:
"""

import math

def catalan_number(n):
    return math.comb(2*n, n) // (n+1)

#test case
print(catalan_number(10))

#output: 16796
<jupyter_output>
16796
<jupyter_text>
**Question 2:**
<jupyter_code>
