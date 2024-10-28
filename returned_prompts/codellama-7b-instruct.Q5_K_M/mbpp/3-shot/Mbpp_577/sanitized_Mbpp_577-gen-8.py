def last_Digit_Factorial(n):
    if n == 0 or n == 1:
        return n
    else:
        while n % 10 == 0:
            n //= 10
        return n % 10