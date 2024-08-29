"""
This function will return the last digit of the factorial of a given number.
"""

def last_Digit_Factorial(n):
    if n==0:
        return 1
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact%10

print(last_Digit_Factorial(4)) # Expected output: 4

