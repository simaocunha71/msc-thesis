```
def skjkasdkd(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    max_prime = max([x for x in lst if is_prime(x)])
    return sum(int(digit) for digit in str(max_prime))
```



This function first defines a helper function `is_prime` to check if a number is prime. It then uses a list comprehension to find the largest prime number in the input list. Finally, it converts the prime number to a string, iterates over each character (digit) in the string, converts each character back to an integer, and returns the sum of these digits.