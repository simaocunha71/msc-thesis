```
def sum(a, b):
    def divisors(n):
        return [i for i in range(1, n+1) if n % i == 0]

    common_divisors = set(divisors(a)) & set(divisors(b))
    return sum(common_divisors)
```


Explanation:
This function first defines a helper function `divisors` that generates all divisors of a given number. Then it finds the common divisors of the two input numbers by taking the intersection of their sets of divisors. Finally, it returns the sum of these common divisors.

The unit test `assert sum(10,15) == 6` ensures that the function is working correctly. For the input numbers 10 and 15, the function should return 6, which is the sum of their common divisors (1, 3 and 5). 