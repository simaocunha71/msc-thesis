Here is a Python solution for the problem. This function checks each number in the list to see if it is prime, and if it is, it calculates the sum of its digits.

```
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

This function works by defining a helper function `is_prime` that checks if a number is prime. It then iterates over the list of numbers, checking each one to see if it is prime and if it is larger than the current maximum prime number. If it is, it updates the maximum prime number. Finally, it returns the sum of the digits of the maximum prime number. The sum of the digits is calculated by converting the number to a string, then iterating over the characters in the string and converting each one back to an integer. The sum of these integers is then returned.