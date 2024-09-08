def last_Digit_Factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        while result % 10 == 0:
            result //= 10
        result %= 1000000000
    return result % 10

print(last_Digit_Factorial(4)) # 4

This solution works by multiplying each number from 1 to n (inclusive) to the result, and then reducing the result to its last digit by using modulo 10 operation. It also reduces the number to its last non-zero digit by continually dividing it by 10 until it is no longer divisible by 10.

The reason we need this is because a trailing zero in the factorial is caused by multiplication by 2 and 5, and any number ending in 5 will cause a trailing zero. Therefore, to find the last digit of the factorial of a number, we only need to consider the numbers ending in 2, 3, 4, 6, 7, 8, and 9. This is why we multiply by i modulo 10 and keep reducing the result until it is no longer divisible by 10.

Also, the result might be very large, so we reduce the result modulo 1000000000 after each multiplication to prevent overflow.

Finally, we return the last digit of the result by taking the modulo 10 of the result.
"""

def last_Digit_Factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        while result % 10 == 0:
            result //= 10
        result %= 1000000000
    return result % 10
"""
This function works by multiplying each number from 1 to n (inclusive) to the result, and then reducing the result to its last digit by using modulo 10 operation. It also reduces the number to its last non-zero digit by continually dividing it by 10 until it is no longer divisible by 10.

The reason we need this is because a trailing