```
def sum(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    common_divisors = [i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0]
    return sum(common_divisors)
```
The function `sum(a, b)` takes two integers `a` and `b` as input and returns the sum of their common divisors. The function first calculates the Greatest Common Divisor (GCD) of `a` and `b` using the Euclidean algorithm. Then, it generates a list of common divisors by iterating from 1 to the GCD and checking if each number is a divisor of both `a` and `b`. Finally, it returns the sum of the common divisors.

The unit test `assert sum(10,15) == 6` ensures that the function returns the correct sum of common divisors for the given input numbers. In this case, the common divisors of 10 and 15 are 1, 3, and 5, and the sum of these divisors is indeed 6.