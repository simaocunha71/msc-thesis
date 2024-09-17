```
def sum(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    common_divisors = [i for i in range(1, min(a, b)+1) if a % i == 0 and b % i == 0]
    return sum(common_divisors)
```


The function `sum(a, b)` calculates the sum of common divisors of two numbers `a` and `b`. It uses a helper function `gcd(a, b)` to calculate the greatest common divisor of `a` and `b`. Then it generates a list of common divisors by iterating over the numbers from 1 to the minimum of `a` and `b`, and checks if each number is a divisor of both `a` and `b`. Finally, it returns the sum of the common divisors. The unit test `assert sum(10,15) == 6` checks that the function returns the correct result for the given inputs. 





```
def sum(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    common_divisors = [i for i in range(1, min(a, b)+1) if a % i == 0 and b % i == 0]
    return sum(common_divisors)
```





```
def sum(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    common_divisors = [i for i in range(1, min(a, b)+1) if a % i == 0 and b % i == 0]
    return sum(common_divisors)
```





```
def sum(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    common_divisors = [i for i in range(1, min(a, b)+1) if a % i == 0 and b % i == 0]
    return sum(common_divisors)
```





```
def sum(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    common_divisors = [i for i in range(1, min(a, b)+1) if a % i