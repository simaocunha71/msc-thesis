The Eulerian number a(n, m) is defined as the sum of products of binomial coefficients. It can be calculated using the following formula:

a(n, m) = Σ((-1)^k * (n-k) choose m) for k from 0 to n

Here is a Python function that calculates the Eulerian number:

```python
def eulerian_num(n, m):
    result = 0
    for k in range(n+1):
        if k % 2 == 0:
            result += math.comb(n-k, m)
        else:
            result -= math.comb(n-k, m)
    return result
```

This function uses the `math.comb` function to calculate the binomial coefficients, which is available in Python 3.8 and later. For earlier versions of Python, you can use the `math.factorial` function to calculate the binomial coefficients:

```python
import math

def math_comb(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

def eulerian_num(n, m):
    result = 0
    for k in range(n+1):
        if k % 2 == 0:
            result += math_comb(n-k, m)
        else:
            result -= math_comb(n-k, m)
    return result
```


The unit test `assert eulerian_num(3, 1) == 4` helps to verify the correctness of the function. It checks that the function returns the correct value for the Eulerian number a(3, 1). If the function is implemented correctly, this test should pass. If the function is incorrect, the test will fail and provide an error message indicating the incorrect result. This helps to debug and test the function.