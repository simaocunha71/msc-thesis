    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return round(area, 2)
    else:
        return -1

