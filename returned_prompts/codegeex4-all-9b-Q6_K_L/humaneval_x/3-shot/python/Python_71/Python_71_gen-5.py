    if a + b > c and a + c > b and b + c > a:
        semi_perimeter = (a + b + c) / 2
        area = (semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5
        return round(area, 2)
    else:
        return -1

