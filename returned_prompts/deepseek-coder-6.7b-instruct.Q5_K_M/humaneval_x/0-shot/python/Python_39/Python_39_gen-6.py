
```python
def prime_fib(n: int):
    def is_prime(num: int):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fib(n: int):
        fib_values = [0, 1]
        for i in range(2, n + 1):
            fib_values.append(fib_values[i - 1] + fib_values[i - 2])
        return fib_values[n]

    count = 0
    num = 0
    while count < n:
        num += 1
        if is_prime(fib(num)):
            count += 1
    return fib(num)
```

Test cases:

```python
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```

This solution works by first defining a helper function to determine if a number is prime. It then defines another helper function to compute the nth Fibonacci number. The main function `prime_fib` generates Fibonacci numbers and increments a counter each time it finds a prime number. It continues this process until it has found the nth prime Fibonacci number.

This solution has a time complexity of O(n^2) due to the nested loops and it has a space complexity of O(n) because it stores the Fibonacci values up to n.

Please note that this solution assumes that the input is a positive integer greater than or equal to 1. If the input can be less than 1, you would need to add error checking.
"""

# Test Cases:

print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))