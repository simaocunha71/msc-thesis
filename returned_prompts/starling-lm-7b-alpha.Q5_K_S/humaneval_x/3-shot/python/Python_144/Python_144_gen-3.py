    numerator_x, denominator_x = x.split("/")
    numerator_n, denominator_n = n.split("/")
    numerator_simplified = numerator_x * int(numerator_n)
    denominator_simplified = denominator_x * int(denominator_n)

    if numerator_simplified % denominator_simplified == 0:
        return True
    else:
        return False


