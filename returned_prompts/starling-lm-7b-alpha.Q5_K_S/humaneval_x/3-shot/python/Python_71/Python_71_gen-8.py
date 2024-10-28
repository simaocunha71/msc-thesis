    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return -1

    # semi-perimeter
    s = (a + b + c) / 2

    # area
    area = (s * (s-a) * (s-b) * (s-c)) ** 0.5

    return round(area, 2)


