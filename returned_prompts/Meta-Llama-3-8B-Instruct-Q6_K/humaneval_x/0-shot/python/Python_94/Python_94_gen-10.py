```
def skjkasdkd(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    max_prime = 0
    for num in lst:
        if is_prime(num) and num > max_prime:
            max_prime = num

    return sum(int(digit) for digit in str(max_prime))
```


This function first defines a helper function `is_prime` to check if a number is prime. It then iterates over the input list, finds the largest prime number, and returns the sum of its digits. The sum of the digits is calculated by converting the prime number to a string, iterating over the characters in the string (which are the digits of the prime number), and summing them up.