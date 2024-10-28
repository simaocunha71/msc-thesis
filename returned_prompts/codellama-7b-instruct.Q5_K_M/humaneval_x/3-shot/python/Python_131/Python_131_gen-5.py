    product = 1
    n = str(n)
    for digit in n:
        if int(digit) % 2 != 0:
            product *= int(digit)
    return product


