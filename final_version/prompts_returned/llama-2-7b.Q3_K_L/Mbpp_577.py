"""
Write a python function to find the last digit in factorial of a given number.
assert last_Digit_Factorial(4) == 4
"""

def last_Digit_Factorial(n):
    if n<1 or n>9:
        return -2
    if n<=5 and (n%5==0 or n%3==0):
        return n-1
    else:
        factorial = 1;
        for i in range(6,n+1):
            factorial *= i
        if (factorial<9**8) and (n>9):
            res=1
            while True:
                if factorial%10==0:
                    return last_Digit_Factorial(res)+1
                else:
                    res+=2
                factorial=factorial//10
        return -1

print(last_Digit_Factorial(4))