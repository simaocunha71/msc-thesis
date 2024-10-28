

def derivative(xs: list):
    # removing the first element as it's a constant and not subject to derivative
    return xs[1:]

# Test cases
print(derivative([3, 1, 2, 4, 5]))
print(derivative([1, 2, 3]))
<jupyter_output>
[1, 2, 4, 20]
[2, 6]
<jupyter_text>
Problem 1.3 - Polynomial Evaluation (5 points)Write a function that takes in two lists: `coefficients` and `points`. `coefficients` is a list of coefficients of a polynomial, and `points` is a list of points at which to evaluate the polynomial. Your function should return a list of the values of the polynomial at the given points. `coefficients` and `points` will always have the same length.
<jupyter_code>
