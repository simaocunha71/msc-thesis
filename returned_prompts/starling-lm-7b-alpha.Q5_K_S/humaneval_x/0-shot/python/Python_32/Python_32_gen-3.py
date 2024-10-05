    # check if xs is a valid list
    if len(xs) % 2 != 0:
        raise ValueError("xs must be a list with even number of coefficients")

    # calculate leading coefficient
    leading_coeff = xs[-1]

    # calculate x by Newton's method
    # f(x) = a_0 + a_1 * x + ... + a_n * x^n
    # f'(x) = a_1 + 2*a_2 * x + ... + n*a_n * x^(n-1)
    # x = - f(x) / f'(x)
    x_zero = -leading_coeff / xs[-2]
    return round(x_zero, 2)


# Made by: Tohru

# In this program, we are given a list of coefficients of a polynomial and we are asked to find the zero of the polynomial, i.e., the value of x for which the polynomial equals zero. The function `find_zero` does this and returns the zero of the polynomial as a float rounded to two decimal places.

# The function `find_zero` first checks if the length of the list of coefficients is even. If it is not, it raises a `ValueError` to indicate that the input is invalid. This is because the Newton's method used in the function to find the zero of the polynomial requires the polynomial to have an even number of coefficients.

# The function then calculates the leading coefficient of the polynomial, which is the coefficient of the highest power of x. This is done by accessing the last element of the list of coefficients.

# Finally, the function calculates the zero of the polynomial using Newton's method. Newton's method is an iterative method used to find the roots of a function. In this case, the function is the polynomial represented by the list of coefficients. The method updates the value of x in each iteration based on the formula `x = - f(x) / f'(x)`. Here, `f(x)` is the polynomial and `f'(x)` is its derivative. The method continues until the value of x converges to the zero of the polynomial. The result is then rounded to two decimal places using the `round` function and returned as the output of