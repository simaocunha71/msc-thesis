
def last_Digit_Factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact % 10

print(last_Digit_Factorial(4))


"""
Explanation:
1. If the number is zero, the factorial is 1.
2. For other numbers, we calculate the factorial by multiplying the number from 1 to the given number.
3. The last digit of a number is given by the remainder when the number is divided by 10. So we return the remainder of the factorial divided by 10.
"""
<jupyter_output>
24
<jupyter_text>
Problem 3
<jupyter_code>
