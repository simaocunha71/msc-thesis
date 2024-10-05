
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def fib(n):
        fib_values = [0, 1]
        for i in range(2, n + 1):
            fib_values.append(fib_values[i-1] + fib_values[i-2])
        return fib_values[n]

    count = 0
    num = 0
    while count < n:
        num += 1
        if is_prime(fib(num)):
            count += 1
    return fib(num)


if __name__ == "__main__":
    import doctest
    doctest.testmod()


The function `prime_fib(n: int)` takes an integer input `n` and returns the n-th number in the Fibonacci sequence that is also a prime number. The helper functions `is_prime(n)` and `fib(n)` are used to check if a number is prime and to calculate the n-th Fibonacci number respectively. The while loop iterates until it finds `n` prime Fibonacci numbers. The function then returns the last found prime Fibonacci number.
"""

# %%
# Test Cases
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
print(prime_fib(6))  # 233
print(prime_fib(7))  # 1597
print(prime_fib(8))  # 28657
print(prime_fib(9))  # 514229
print(prime_fib(10))  # 433494437

# %%
# End of File

