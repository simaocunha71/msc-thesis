The Eulerian number a(n, m) is defined as the coefficient of the term x^(n-m) in the polynomial (x + 1)^n. It can be calculated using the following formula:

a(n, m) = (n-1)! / (m-1)! * (n-m+1) * (n-m+2) * ... * n

Here is a Python function that calculates the Eulerian number:

```python
import math

def eulerian_num(n, m):
    result = math.factorial(n-1) // math.factorial(m-1)
    for i in range(m, n):
        result *= i
    return result
```

This function uses the math.factorial function to calculate the factorials and the // operator to perform integer division. The result is then multiplied by the remaining factors (n-m+1) to (n) and returned.

The unit test `assert eulerian_num(3, 1) == 4` is used to verify that the function returns the correct value for the Eulerian number a(3, 1). This test can be used to check the correctness of the function for other values of n and m as well.