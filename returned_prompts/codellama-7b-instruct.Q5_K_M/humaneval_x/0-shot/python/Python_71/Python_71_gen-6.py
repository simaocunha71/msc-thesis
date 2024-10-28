
    import math
    a = float(a)
    b = float(b)
    c = float(c)
    if a + b > c and b + c > a and c + a > b:
        s = (a + b + c) / 2
        return round(math.sqrt(s * (s - a) * (s - b) * (s - c)), 2)
    else:
        return -1
