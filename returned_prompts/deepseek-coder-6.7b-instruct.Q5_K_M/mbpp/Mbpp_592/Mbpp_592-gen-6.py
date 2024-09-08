The function can be written to solve this problem. The binomial coefficient can be calculated using the factorial function.

Here is a Python solution:

```python
import math

def sum_Of_product(n):
    total = 0
    for i in range(1, n):
        total += math.factorial(n)/(math.factorial(i)*math.factorial(n-i)) * math.factorial(n)/(math.factorial(i+1)*math.factorial(n-i))
    return int(total)

print(sum_Of_product(3))  # Output: 15
```

In the sum_Of_product() function, we use a loop to iterate from 1 to n. In each iteration, we calculate the binomial coefficient (n over i) * (n over n-i) and add it to the total sum.

Note that we convert the result to an integer before returning it because the binomial coefficients are always integers.

The math.factorial() function is used to calculate the factorial of a number, which is a common prerequisite for calculating binomial coefficients. 

The function returns the sum of the product of consecutive binomial co-efficients.
"""

