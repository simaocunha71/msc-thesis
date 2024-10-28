def last_Digit_Factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        while n:
            result = (result * n) % 10
            n -= 1
        return result