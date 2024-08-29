This question asks to solve for the zero of a polynomial function using a numerical method. Here is a Python solution using the Newton-Raphson method:

```python
def find_zero(xs):
    """
    xs are coefficients of a polynomial. find_zero find x such that poly(x) = 0. find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) #f(x) = 1 + 2x 
    -0.5 
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3 
    1.0
    """
    # Define the polynomial function
    def poly(x):
        result = xs[0]
        for i in range(1, len(xs)):
            result += xs[i] * x**i
        return result

    # Define the derivative of the polynomial function
    def poly_prime(x):
        result = xs[1]
        for i in range(2, len(xs)):
            result += i * xs[i] * x**(i-1)
        return result

    # Start from the middle of the range
    x = 0

    # Iterate until we reach a zero
    while abs(poly(x)) > 1e-6:
        x = x - poly(x) / poly_prime(x)

    return x
```
This solution uses the Newton-Raphson method to find the root of a function. This method is an iterative technique that starts with an initial guess and then iteratively improves this guess until it converges to a root. The method works by approximating the function with its tangent line at the current guess and then finding the root of this tangent line. The new guess is then this root, and the process is repeated until the function value is sufficiently small.