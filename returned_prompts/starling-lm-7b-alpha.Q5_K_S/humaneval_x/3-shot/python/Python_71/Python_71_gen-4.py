    if (a + b > c and b + c > a and c + a > b):
        s = (a + b + c) / 2.0
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return "{:.2f}".format(round(area, 2))
    else:
        return -1


