```
def sum_series(n):
    return sum(n - 2*i for i in range(n//2 + 1))
```


Explanation:
The problem is asking for a function that calculates the sum of the series n - 2*i, where i goes from 0 to n//2. This is a simple arithmetic series, and we can use the formula for the sum of an arithmetic series to solve this.

The formula for the sum of an arithmetic series is:

sum = (n/2) * (2a + (n-1)d)

where n is the number of terms, a is the first term, and d is the common difference.

In this case, the first term is n, the common difference is -2, and the number of terms is n//2 + 1 (because the last term is n//2, and we want to include it in the sum).

So, we can use this formula to calculate the sum:

sum = (n//2 + 1) * (2n - (n//2 + 1)*2)

Simplifying this expression, we get:

sum = n

So, the function sum_series(n) should simply return n.

The unit test assert sum_series(6) == 12 confirms this. When n is 6, the sum of the series is 12, which is indeed equal to n.