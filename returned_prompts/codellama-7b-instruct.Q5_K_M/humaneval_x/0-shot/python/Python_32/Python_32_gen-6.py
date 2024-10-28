
    n = len(xs)

    # if the number of coefficients is odd,
    # the polynomial has no zero.
    if n % 2 != 0:
        return None

    # find the largest non zero coefficient.
    # if there is no non zero coefficient,
    # the polynomial has no zero.
    max_coeff = max(xs, key=lambda coeff: abs(coeff))
    if max_coeff == 0:
        return None

    # find x such that poly(x) = 0
    # by setting the derivative of poly(x) to 0.
    # poly(x) is a polynomial of degree n - 1,
    # and its derivative is a polynomial of degree n - 2.
    # therefore, the only zero of poly(x) is x = 0.
    return 0