The binomial co-efficients are given by the formula:

C(n,k) = nC(k) = nC(n-k)

where nC(k) represents the binomial coefficient.

The product of consecutive binomial co-efficients can be computed as:

(n-1)C(k-1) * nC(k)

We can sum these products up to get our result.

Here's a python function that achieves this:

```python
def sum_Of_product(n):
    product_sum = 0
    for k in range(1, n):
        product = binomial_coefficient(n-1, k-1) * binomial_coefficient(n, k)
        product_sum += product
    return product_sum
```

The `binomial_coefficient` function is a helper function that computes the binomial coefficient. It is implemented using the factorial function:

```python
def binomial_coefficient(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))
```

And the `factorial` function is implemented as follows:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

This function works by iterating over the range of `k` values from 1 to `n-1`, and for each `k`, it computes the product of the binomial coefficients `(n-1)C(k-1)` and `nC(k)`, adds this product to the running total `product_sum`, and finally returns `product_sum` once the loop has finished.
"""

# ---------------------
# Code

def binomial_coefficient(n, k):
    if k>n:
        return 0
    if k==0 or k==n:
        return 1
    else:
        return factorial(n) / (factorial(k) * factorial(n - k))

def factorial(n):
    if n == 0:
