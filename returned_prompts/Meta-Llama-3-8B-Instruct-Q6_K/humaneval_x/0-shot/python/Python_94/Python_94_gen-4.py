```
def skjkasdkd(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    max_prime = 0
    for num in lst:
        if is_prime(num) and num > max_prime:
            max_prime = num

    if max_prime == 0:
        return 0
    return sum(int(digit) for digit in str(max_prime))
```


This function first defines a helper function `is_prime` to check if a number is prime. Then, it iterates over the input list to find the largest prime number. If no prime numbers are found, it returns 0. Finally, it calculates the sum of the digits of the largest prime number and returns the result.