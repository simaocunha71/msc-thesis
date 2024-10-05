

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# Test cases
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False

```

This code defines a function `is_prime(n)` that takes an integer `n` as input and returns True if `n` is prime, and False otherwise. The function uses a simple algorithm to check if a number is prime. It first checks if the number is less than or equal to 1, and returns False in that case, as 1 and all numbers less than or equal to 1 are not prime. Then it checks if the number is less than or equal to 3, and returns True in that case, as 2 and 3 are prime. Next, it checks if the number is divisible by 2 or 3, and returns False in that case. After that, it enters a while loop that checks if the square of the current number `i` is less than or equal to the given number `n`. If it is, it checks if `n` is divisible by `i` or `i + 2`, and returns False in that case. Then it increments `i` by 6 and continues the loop. If none of the conditions in the while loop are met, it means that the number is prime, and the function returns True.

The code includes several test cases to demonstrate the usage of the `is_prime` function. It prints the results of the function for various inputs, such as 6, 101, 11, 13441,