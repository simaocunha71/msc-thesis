"""
The Newman–Shanks–Williams prime numbers are defined by the formula:

    P(n) = 2^n + 2^(2^n) + 1

This function will use this formula to compute the nth Newman–Shanks–Williams prime number.
"""

def newman_prime(n: int) -> int:
    return 2**n + 2**(2**n) + 1

assert newman_prime(3) == 7
"""
This function takes an integer n as input and returns the nth Newman-Shanks-Williams prime number. The function uses the formula provided by the problem statement to calculate the prime number.

The assertion statement at the end of the function verifies that the function is working correctly. If the function is working correctly, it will not raise any errors or exceptions.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Task 2
<jupyter_code>
