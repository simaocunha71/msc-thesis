    product = 1
    has_odd = False

    for digit in str(n):
        digit = int(digit)
        if digit % 2 != 0:
            product *= digit
            has_odd = True

    return product if has_odd else 0

