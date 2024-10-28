    product = 1
    is_odd_digit = False
    while n != 0:
        digit = n % 10
        n //= 10
        if digit % 2 != 0:
            if is_odd_digit:
                product *= digit
            else:
                is_odd_digit = True
                product = digit
    return product


