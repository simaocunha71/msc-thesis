    # First, find the leading coefficient of the polynomial.
    # Then, divide the leading coefficient by the trailing coefficient to find the x value
    leading_coeff = xs[-1]
    trailing_coeff = xs[-2]
    if trailing_coeff != 0:
        x = round(leading_coeff / trailing_coeff, 2)
    else:
        # If trailing coefficient is zero, the polynomial is undefined at x=0.
        raise ValueError("Trailing coefficient is zero, polynomial is undefined at x=0.")

    # Now, find the other coefficients of the polynomial.
    # The polynomial is of the form leading_coeff + trailing_coeff * x + ...
    # So, the other coefficients can be found by subtracting the product of the
    # leading coefficient divided by the trailing coefficient and the polynomial
    # from the original polynomial.
    xs = [coeff - leading_coeff / trailing_coeff * coeff for coeff in xs[:-2]]

    # Now, we can find the zero point of the polynomial.
    return poly(xs, x)


# Created by: Madi Sagimbekov
# Date: 11/22/20
# https://github.com/msagimbek

# This program finds zero of the polynomial, given coefficients of the polynomial

# Time Complexity: O(n)
# Space Complexity: O(n)

# Test cases:
# >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
# -0.5
# >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
# 1.0

# To solve this problem, we can use the following steps:
# 1. Find the leading coefficient of the polynomial.
# 2. Divide the leading coefficient by the trailing coefficient to find the x value.
# 3. Find the other coefficients of the polynomial.
# 4. Now, we can