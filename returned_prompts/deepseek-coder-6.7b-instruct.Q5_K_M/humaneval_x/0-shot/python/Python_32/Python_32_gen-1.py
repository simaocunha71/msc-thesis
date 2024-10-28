This problem requires a numerical method to find the roots of a polynomial equation. However, Python's math library does not provide a method to find the roots of a polynomial equation, so we will use the Bisection method.

The Bisection method is a root-finding method that applies to any continuous function for which one knows two values with opposite signs.

Here is the Python code:

```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1]  * x  ... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    def bisection(a: float, b: float):
        """
        Finds a root of the polynomial in the interval [a, b].
        """
        if poly(xs, a) * poly(xs, b) >= 0:
            print("Bisection method fails.")
            return None
        else:
            c = a
            while (b-a) >= 0.01:
                # Find middle point
                c = (a+b)/2

                # Check if middle point is root
                if poly(xs, c) == 0.0:
                    break

                # Decide the side to repeat the steps
                if poly(xs, c) * poly(xs, a) < 0:
                    b = c
                else:
                    a = c
            return c

    # Find initial guesses for the roots by looking for changes of sign
    for i in range(len(xs) - 1):
        if xs[i] != xs[i+1]:
            return bisection