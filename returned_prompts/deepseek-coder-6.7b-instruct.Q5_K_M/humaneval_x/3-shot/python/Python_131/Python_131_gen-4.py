    product = 1
    for d in str(n):
        if int(d) % 2 != 0:
            product *= int(d)
    return product


