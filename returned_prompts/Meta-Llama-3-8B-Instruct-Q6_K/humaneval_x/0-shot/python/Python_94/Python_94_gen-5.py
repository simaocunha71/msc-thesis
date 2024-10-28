```
def skjkasdkd(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    max_prime = max([i for i in lst if is_prime(i)])
    return sum(int(digit) for digit in str(max_prime))
```



Explanation:
This solution defines a helper function `is_prime` to check if a number is prime. It then uses a list comprehension to find the largest prime number in the input list `lst`. Finally, it converts the largest prime number to a string, iterates over each character (digit) in the string, converts each character back to an integer, and returns the sum of these digits.

The `is_prime` function works by checking if a number is divisible by any integer between 2 and the square root of the number. If it is, then the number is not prime. If it's not divisible by any of these integers, then it's prime.

The list comprehension `[i for i in lst if is_prime(i)]` finds all prime numbers in the input list `lst`. The `max` function then returns the largest of these prime numbers.

The expression `sum(int(digit) for digit in str(max_prime))` converts the largest prime number to a string, then iterates over each character (digit) in the string, converts each character back to an integer, and returns the sum of these digits. This is the sum of the digits of the largest prime number.