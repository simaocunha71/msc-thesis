    even_digits = []
    for i in range(min(a, b), max(a, b) + 1):
        if i % 2 == 0:
            even_digits.append(i)
    return even_digits


