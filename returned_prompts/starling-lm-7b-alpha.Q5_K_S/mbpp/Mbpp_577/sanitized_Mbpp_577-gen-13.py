def last_Digit_Factorial(n):
    if n == 0:
        return 1
    else:
        res = 1
        while n > 0:
            res = (res * n) % 10
            n -= 1
        return res