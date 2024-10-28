Here is a Python solution for the problem:
```python
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

    if max_prime == 0:
        return 0
    else:
        return sum(int(digit) for digit in str(max_prime))
```
The function `skjkasdkd` takes a list of integers as input and returns the sum of the digits of the largest prime number in the list. The `is_prime` function checks whether a given number is prime or not. If the largest prime number is 0, the function returns 0. Otherwise, it converts the largest prime number to a string, and then sums up the digits of the string.