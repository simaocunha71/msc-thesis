
    def is_prime(n: int):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def fib(n: int):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    count = 0
    i = 1
    while True:
        f = fib(i)
        if is_prime(f):
            count += 1
            if count == n:
                return f
        i += 1


print(prime_fib(1))
print(prime_fib(2))
print(prime_fib(3))
print(prime_fib(4))
print(prime_fib(5))
print(prime_fib(6))
print(prime_fib(7))
print(prime_fib(8))
print(prime_fib(9))
print(prime_fib(10))

# Output:
# 2
# 3
# 5
# 13
# 89
# 233
# 1597
# 28657
# 514229
# 433494437


```

Explaination:
The function `prime_fib` generates Fibonacci numbers one at a time and checks whether each one is prime. If it is, it increments a counter. When the counter reaches the input number `n`, it returns the corresponding Fibonacci number.

The helper functions `is_prime` and `fib` are used to check if a number is prime and generate Fibonacci numbers respectively. The function `is_prime` checks whether a number is prime by iterating from 2 to the square root of the number and checking for divisibility. If any number in this range divides the number evenly, the function returns `False`, otherwise it returns `True`.

The function `fib` generates Fibonacci numbers using a simple loop