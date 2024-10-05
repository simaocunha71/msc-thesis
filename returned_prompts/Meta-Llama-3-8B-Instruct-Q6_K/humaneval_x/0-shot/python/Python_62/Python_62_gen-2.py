    return [i * xs[i] for i in range(1, len(xs))]
    # This function takes a list of coefficients of a polynomial
    # and returns the list of coefficients of the derivative of the polynomial.
    # The derivative of a polynomial is calculated by multiplying each coefficient
    # with its corresponding power of the variable (x), and then shifting the powers by one.
    # This is implemented in the list comprehension: i * xs[i] for i in range(1, len(xs)).
    # The range function is used to generate the powers of the variable (x), starting from 1
    # (because the derivative of x^0 is 0, so the first coefficient is ignored)
    # and ending at the length of the list (because the derivative of x^n is n*x^(n-1), so
    # the last coefficient is multiplied by its power and then the list is truncated).
    # The result is a new list of coefficients, representing the derivative of the original polynomial.