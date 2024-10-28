    numerator_x, denominator_x = [int(x) for x in x.split('/')]
    numerator_n, denominator_n = [int(x) for x in n.split('/')]
    lcm = numerator_x * denominator_n
    result = lcm // denominator_x * numerator_n

    if result % 1 == 0:
        return True
    else:
        return False


