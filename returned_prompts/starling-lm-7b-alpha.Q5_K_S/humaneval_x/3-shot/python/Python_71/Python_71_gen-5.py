    if not (a+b>c and a+c>b and b+c>a):
        return -1
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return round(area, 2)


