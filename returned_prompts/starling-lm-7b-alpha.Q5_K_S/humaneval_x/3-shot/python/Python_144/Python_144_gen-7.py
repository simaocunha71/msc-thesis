    numerator_x, denominator_x = x.split('/')
    numerator_n, denominator_n = n.split('/')

    numerator = int(numerator_x) * int(numerator_n)
    denominator = int(denominator_x) * int(denominator_n)

    gcd = 0
    for i in range(1, min(numerator,denominator)+1):
        if numerator % i == 0 and denominator % i == 0:
            gcd = i

    return numerator // gcd == denominator // gcd


