    numerator_x, denominator_x = x.split('/')
    numerator_n, denominator_n = n.split('/')

    numerator_result = int(numerator_x) * int(numerator_n)
    denominator_result = int(denominator_x) * int(denominator_n)

    if numerator_result % denominator_result == 0:
        return True
    else:
        return False


