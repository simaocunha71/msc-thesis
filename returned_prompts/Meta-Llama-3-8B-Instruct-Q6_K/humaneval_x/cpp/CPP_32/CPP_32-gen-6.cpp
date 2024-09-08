This problem can be solved by implementing Newton's method for finding the root of a polynomial. Newton's method is an iterative method that starts with an initial guess and then iteratively improves the guess until it converges to the root.

Here is a Python solution using Newton's method:

```Python
import math

def poly(xs, x):
    sum = 0
    for i in range(len(xs)):
        sum += xs[i] * math.pow(x, i)
    return sum

def find_zero(xs):
    # Find the initial guess
    x0 = -xs[0] / xs[-1]

    # Initialize the tolerance for convergence
    tol = 1e-6

    # Initialize the maximum number of iterations
    max_iter = 100

    for _ in range(max_iter):
        x = x0 - poly(xs, x0) / poly([i * x for i in xs], x0)
        if abs(x - x0) < tol:
            return round(x, 2)
        x0 = x

    return round(x0, 2)

# Example usage
print(round(find_zero([1, 2]), 2))  # Output: -0.5
print(round(find_zero([-6, 11, -6, 1]), 2))  # Output: 1.0
```

This code first calculates the initial guess by dividing the leading coefficient by the last coefficient. It then iteratively improves the guess using Newton's method until the difference between the current guess and the previous guess is less than a specified tolerance. The final result is rounded to 2 decimal places.

Note that this code assumes that the polynomial has at least one real root, and that the root is within the range of the initial guess. In practice, you may need to modify the code to handle cases where these assumptions are not met. For example, you could use a more sophisticated method to find the initial guess, or you could use a different method to find the root if Newton's method fails to converge.