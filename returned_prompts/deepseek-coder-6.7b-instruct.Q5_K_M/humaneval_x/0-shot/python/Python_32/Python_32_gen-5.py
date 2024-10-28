The problem can be solved using Bisection method. The Bisection method is a root-finding method that applies to any continuous functions for which one knows two values with opposite signs.

Here is the Python code implementing the Bisection method to solve the polynomial equation:

```python
def bisection(xs, low, high):
    if poly(xs, low) * poly(xs, high) > 0:
        print("You have not assumed right a and b\n")
        return -1

    mid = low
    while (high - low) >= 0.01:
        mid = (high + low) / 2
        if poly(xs, mid) == 0.0:
            break
        else:
            if poly(xs, low) * poly(xs, mid) < 0:
                high = mid
            else:
                low = mid
    return mid

def find_zero(xs):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    # find the range of x where the polynomial changes sign
    low = 0
    high = 1
    while poly(xs, low) * poly(xs, high) > 0:
        low = high
        high *= 2

    # use bisection method to find the root
    return bisection(xs, low, high)

print(find_zero([1, 2]))  # f(x) = x + 2
print(find_zero([-6, 11, -6, 1]))  # f(x) = -6 + x*(11 - 6x + 1)
```

This code first finds a range where the polynomial changes sign, then uses the Bisection method to find the root in that range. The Bisection method works by repeatedly dividing the range in half until the root is found.

Note: The Bisection method may not always converge to a root, especially for polynomials with multiple roots. In such