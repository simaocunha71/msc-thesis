    if len(xs) % 2 == 0:
        # if the number of coefficients is even
        # find the root of the polynomial
        # by using the rational root theorem
        for i in range(1, abs(xs[0]) + 1):
            if abs(xs[0]) % i == 0:
                for j in range(1, abs(xs[-1]) + 1):
                    if abs(xs[-1]) % j == 0:
                        if math.pow(i, len(xs) - 1) % j == 0:
                            result = -i / j
                            if poly(list(map(lambda x: x * result, xs))) < 0.0001:
                                return result
    return 0.0  # default return value


