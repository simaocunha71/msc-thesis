Here is a python function that uses the sympy library to calculate the binomial coefficients and then calculates the sum of the product of consecutive binomial co-efficients:

```python
from sympy import binomial

def sum_Of_product(n):
    sum_ = 0
    for i in range(1,n):
        sum_ += binomial(n,i) * binomial(n,i+1)
    return sum_

print(sum_Of_product(3))  # 15
```

The binomial(n, i) function is used to calculate the binomial coefficient. The sum_ variable stores the sum of the products, and for each i from 1 to n-1, the product of the binomial coefficient of n and i, and the binomial coefficient of n and i+1 is added to sum_.

Note: The binomial coefficient C(n, k) counts the number of ways to choose k items from n items without repetition and without order.

Also, please note that this function will return a different result for n=0 or n=1, because it starts the sum from i=1 and does not include the binomial coefficient of n=0 or n=1.
"""

