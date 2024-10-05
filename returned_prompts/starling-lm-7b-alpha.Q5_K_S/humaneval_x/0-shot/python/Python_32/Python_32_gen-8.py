    coeff = xs[0]
    n = len(xs) // 2
    x = 0
    while coeff != 0:
        if xs[n] < 0:
            x *= -1
        coeff, xs = xs[n], xs[:n]
        n = n - 1
    return x

# Implementation notes:
# In this code, we are assuming that the polynomial is given by the
# coefficients in decreasing order of degree, i.e., the first element of
# the list is the coefficient of the highest degree term, the second element
# is the coefficient of the next highest degree term, and so on.
#
# In other words, if the polynomial is given by:
# f(x) = c_n * x^n + ... + c_1 * x + c_0
# then the coefficients in the list should be given in the order: c_n, c_(n-1), ..., c_1, c_0
#
# As an example, if f(x) = 3 * x^2 + 2 * x + 1, then the list of coefficients should be [3, 2, 1]
# In this case, the code will return the value of x for which f(x) = 0, i.e., the zero of the polynomial.
#
# Here's a breakdown of the code:
# - The variable coeff holds the coefficient of the highest degree term in the polynomial. It is set to the first element of the coefficients list.
# - The variable n holds the degree of the polynomial. It is set to half the length of the coefficients list.
# - The variable x holds the zero of the polynomial. It is set to 0.
# - While the coefficient of the highest degree term in the polynomial is not zero:
#     - If the coefficient of the highest degree term is negative, the zero of the polynomial is negated.
#     - The coefficient of the highest degree term is removed from the coefficients list.
#     - The degree of the polynomial is reduced by 1.
# - The zero of the polynomial is returned.

# This code uses a while loop to repeatedly update the coefficient and the degree of the polynomial until the coefficient of the highest degree term is zero.