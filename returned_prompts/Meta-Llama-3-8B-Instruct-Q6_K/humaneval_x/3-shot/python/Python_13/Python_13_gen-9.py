    while b:
        a, b = b, a % b
    return a
    # or
    # return math.gcd(a, b)
    # (Python 3.5+)


