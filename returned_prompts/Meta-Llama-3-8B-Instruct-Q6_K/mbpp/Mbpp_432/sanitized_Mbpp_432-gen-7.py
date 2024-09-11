def median_trapezium(a, b, c):
    if a <= b <= c:
        return b
    elif a <= c <= b:
        return c
    elif b <= a <= c:
        return a
    elif b <= c <= a:
        return c
    elif c <= a <= b:
        return a
    else:
        return b