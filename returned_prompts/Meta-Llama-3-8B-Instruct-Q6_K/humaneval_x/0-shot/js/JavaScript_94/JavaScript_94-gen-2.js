Here is a Python solution for the problem:

```Python
def skjkasdkd(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    max_prime = 0
    for num in lst:
        if is_prime(num) and num > max_prime:
            max_prime = num

    return sum(int(digit) for digit in str(max_prime))
```

This function first defines a helper function `is_prime` to check if a number is prime. Then it iterates over the list and finds the largest prime number. Finally, it returns the sum of the digits of this prime number. The `is_prime` function uses a simple trial division method to check if a number is prime. It only needs to check up to the square root of the number, because a larger factor of the number would be a multiple of a smaller factor that has already been checked. The `str` function is used to convert the prime number to a string, and then a generator expression is used to iterate over the characters in the string (i.e., the digits of the prime number) and sum them up.