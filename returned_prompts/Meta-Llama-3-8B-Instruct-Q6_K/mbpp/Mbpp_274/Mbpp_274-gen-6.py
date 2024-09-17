The problem is asking to create a function that calculates the sum of binomial coefficients at even indices for a given positive integer n. 

The binomial coefficients are calculated using the formula `n choose r = n! / (r! * (n-r)!)`. The problem doesn't explicitly state this, but we can infer it from the unit test provided, which is `assert even_binomial_Coeff_Sum(4) == 8`. 

Here is the Python function that solves the problem:

```python
from math import comb

def even_binomial_Coeff_Sum(n):
    total_sum = 0
    for i in range(0, n+1, 2):
        total_sum += comb(n, i)
    return total_sum
```

In this function, we initialize a variable `total_sum` to 0. Then, we use a for loop to iterate over the even indices from 0 to n. For each even index `i`, we calculate the binomial coefficient `n choose i` using the `comb` function from the `math` module and add it to `total_sum`. Finally, we return `total_sum`. 

The unit test `assert even_binomial_Coeff_Sum(4) == 8` passes with this function. For `n = 4`, the binomial coefficients at even indices are `4 choose 0 = 1`, `4 choose 2 = 6`, and `4 choose 4 = 1`. The sum of these coefficients is 1 + 6 + 1 = 8, which is what the function returns. 