def get_ludic(n):
    ludic_numbers = [2, 3, 5, 7]
    for i in range(9, n+1):
        ludic_numbers.append(next(x for x in ludic_numbers if (i % x) == 0))
    return ludic_numbers
