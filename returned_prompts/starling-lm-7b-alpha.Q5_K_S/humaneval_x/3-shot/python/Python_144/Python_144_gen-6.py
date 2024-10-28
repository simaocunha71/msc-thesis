    # x = a / b
    # n = c / d
    # We need to find if (a * d) % b == 0

    # Convert both fractions to numeric and gcd them
    numerator_x = int(x.split("/")[0])
    denominator_x = int(x.split("/")[1])
    numerator_n = int(n.split("/")[0])
    denominator_n = int(n.split("/")[1])

    gcd = gcd(denominator_x, denominator_n)
    new_denominator_x = (denominator_x * denominator_n) // gcd
    new_numerator_n = (numerator_n * denominator_x) // gcd
    new_numerator_x = (numerator_x * denominator_n) // gcd

    if new_numerator_n % new_denominator_x == 0:
        return True

    return False


