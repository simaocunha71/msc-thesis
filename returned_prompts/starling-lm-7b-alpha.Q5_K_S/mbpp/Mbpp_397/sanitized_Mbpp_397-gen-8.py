def median_numbers(a,b,c):
    if a<=b<=c:
        return b
    elif c<=a<=b:
        return a
    elif b<=c<=a:
        return c