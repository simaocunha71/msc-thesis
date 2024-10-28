def min_of_three(a, b, c):
    return min(a, b, c) # returns the smallest of the three numbers
    # or
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c