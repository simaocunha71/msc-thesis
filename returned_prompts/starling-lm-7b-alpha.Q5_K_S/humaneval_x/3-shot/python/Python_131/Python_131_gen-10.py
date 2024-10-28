    product = 1
    is_odd = False

    while n != 0:
        d = n % 10
        if d % 2 == 1:
            product *= d
            is_odd = True
        n //= 10

    return product if is_odd else 0


