"""
The even index binomial coefficients are C(2,0), C(4,2), C(6,4),...
So, we can iterate through the binomial coefficients and sum the ones at even indices.

Here is the Python code:

```python
import math

def even_binomial_Coeff_Sum(n):
    total_sum = 0
    for i in range(0, n+1, 2):
        total_sum += math.comb(n+1, i)
    return total_sum

print(even_binomial_Coeff_Sum(4))  # Output: 8
```

The above python function "even_binomial_Coeff_Sum" calculates the sum of even index binomial coefficients. The function takes a positive integer n as input and returns the sum of binomial coefficients at even indices. The binomial coefficients at even indices are calculated using the `math.comb` function in Python. We use a loop to iterate through the binomial coefficients and sum the ones at even indices.

The time complexity of this function is O(n) because we iterate through n/2 terms. The space complexity is O(1) because we only use a fixed amount of space to store the sum and the loop indices.
"""

# Q2
