```
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
    return 1  # in case n is a prime number
```


This function iterates over all numbers from n-1 down to 1 and checks if the number is a divisor of n. If it finds a number that is a divisor, it returns that number. If no divisor is found (i.e., n is a prime number), it returns 1. The `range` function is used to generate the numbers from n-1 down to 1, and the `for` loop iterates over these numbers. The `if` statement checks if the current number is a divisor of n by using the modulus operator (`%`). If the remainder is 0, then the number is a divisor, and the function returns that number. If no divisor is found, the function returns 1. The `>>> largest_divisor(15)` comment indicates that the function should return 5 when given the input 15.