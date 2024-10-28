def is_undulating(n):
    a, b = 1, 1
    while n > 0:
        if n == 1:
            return True
        if n < 1:
            return False
        d = n % 10
        if d == 9:
            a, b = b, a+b
        elif d == 0:
            return False
        n //= 10
    return True