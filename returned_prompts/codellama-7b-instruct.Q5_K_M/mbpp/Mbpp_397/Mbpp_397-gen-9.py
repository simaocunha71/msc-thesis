
def median_numbers(a, b, c):
    s1 = a + b + c
    s2 = s1 - min(a, b, c)
    return max(s1 - s2, s2 - min(s1 - s2, a, b, c))


