    if a + b <= c or a + c <= b or b + c <= a:
        return -1

    semi_perimeter = (a + b + c) / 2
    area = (semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5
    return round(area, 2)

