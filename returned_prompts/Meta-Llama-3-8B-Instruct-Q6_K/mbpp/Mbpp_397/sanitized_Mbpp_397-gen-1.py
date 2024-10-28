def median_numbers(a, b, c):
    if a <= b <= c or c <= b <= a:
        return b
    elif a <= c <= b or b <= c <= a:
        return c
    else:
        return a