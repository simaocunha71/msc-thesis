    product = 1
    found_odd = False

    for digit in str(n):
        digit = int(digit)

        if digit % 2 != 0:
            product *= digit
            found_odd = True

    return product if found_odd else 0


