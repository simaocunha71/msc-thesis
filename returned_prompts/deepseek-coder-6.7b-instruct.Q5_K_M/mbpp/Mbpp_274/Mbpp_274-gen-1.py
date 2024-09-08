Here is the python function that solves the problem:

```python
def even_binomial_Coeff_Sum(n):
    result = 0
    for i in range(0, n+1, 2):
        result += binom(n, i)
    return result

print(even_binomial_Coeff_Sum(4))  # Output: 8
```
This function first calculates the binomial coefficient using the binom function from the math module. Then it sums up the binomial coefficients at even indices.
"""

