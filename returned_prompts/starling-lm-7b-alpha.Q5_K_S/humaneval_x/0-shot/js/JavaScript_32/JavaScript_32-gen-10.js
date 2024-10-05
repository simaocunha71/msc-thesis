To solve a polynomial equation of degree 2n, you can use Newton's method, which is an iterative method. Here's a step-by-step guide:

1. Define an initial guess for the root, x₀. It's typically chosen to be the average of the roots of the polynomial.
2. Calculate the value of the polynomial at this guess, p(x₀).
3. Evaluate the derivative of the polynomial at this guess, p'(x₀). If p'(x₀) = 0, then the algorithm is finished. Otherwise, continue to the next step.
4. Calculate the next guess for the root, x₁ = x₀ - p(x₀) / p'(x₀).
5. Repeat steps 2-4 until the value of the polynomial at the guess is sufficiently close to 0.

Here's a Python function that implements the above algorithm:

```python
def find_zero(xs):
    def poly(x):
        return reduce(lambda prev, item, index: prev + item * pow(x, index), xs, 0)
    def derivative(xs):
        return [n * x ** (n - 1) for n, x in enumerate(xs)]
    x = 0.0
    while abs(poly(x)) > 1e-6:
        p = poly(x)
        p_prime = derivative(xs)
        x = x - p / p_prime
    return x
```

In this function, `poly` is a function that evaluates the polynomial at a given point, and `derivative` is a function that evaluates the derivative of the polynomial at a given point. The main loop iterates until the absolute value of the polynomial at the guess is less than 1e-6, which is a small number that determines the precision of the calculation.

Finally, the function returns the root of the polynomial.

Keep in mind that Newton's method is an iterative method, which means it may not converge to a solution in some cases. However, for a polynomial of degree 2n, it's a reliable method to find a root.

Here's a Python function that implements the above algorithm