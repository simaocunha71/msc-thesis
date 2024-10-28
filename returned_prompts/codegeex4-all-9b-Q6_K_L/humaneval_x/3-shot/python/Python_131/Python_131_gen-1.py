    product = 1
    is_odd = False

    for digit in str(n):
        if int(digit) % 2 != 0:
            is_odd = True
            product *= int(digit)

    return 0 if not is_odd else product

