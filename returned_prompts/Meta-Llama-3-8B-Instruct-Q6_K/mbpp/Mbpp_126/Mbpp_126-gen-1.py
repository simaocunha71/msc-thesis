```
def sum(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    common_divisors = [i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0]
    return sum(common_divisors)
``` 
The function `sum(a, b)` finds the sum of common divisors of two given numbers `a` and `b`. 
It uses the helper function `gcd(a, b)` to find the greatest common divisor of `a` and `b`. 
Then it generates a list of common divisors by iterating over the range from 1 to the minimum of `a` and `b` and checks if `a` and `b` are divisible by the current number. 
Finally, it returns the sum of the common divisors. 

The unit test `assert sum(10,15) == 6` ensures that the function works correctly for the given inputs. 
For the inputs 10 and 15, the common divisors are 1, 3 and 5, and their sum is 9, not 6. 
This is a bug in the function. 
The function should be corrected to return the sum of all divisors, not just the common divisors. 
The corrected function is as follows:

```
def sum(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    def divisors(n):
        result = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                result.append(i)
                if i * i != n:
                    result.append(n // i)
        return result
    a_divisors = set(divisors(a))
    b_divisors = set(divisors(b))
    return sum(a_divisors & b_divisors)
```

This function first finds the greatest common divisor of `a` and `b` using the `gcd` function. 
Then it finds the divisors of `a` and `b` using the `divisors` function. 
The function `divisors(n)` returns a list of divisors of `n`. 
It does this by iterating over the range from 1 to the square root of `n` and checks if `n`