
def digits(n):
    if n < 1:
        return 0
    result = 1
    while n > 0:
        d = n % 10
        if d % 2 == 1:
            result *= d
        n //= 10
    return result

