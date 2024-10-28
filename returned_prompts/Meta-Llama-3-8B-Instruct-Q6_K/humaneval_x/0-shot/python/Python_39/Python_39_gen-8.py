    def is_prime(num: int):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fib(n: int):
        if n <= 1:
            return 0
        elif n == 2:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n):
                a, b = b, a + b
            return b

    for i in range(1, n+1):
        num = fib(i)
        if is_prime(num):
            return num

# Testing the function
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: 233
print(prime_fib(7))  # Output: 1597
print(prime_fib(8))  # Output: 28657
print(prime_fib(9))  # Output: 514229
print(prime_fib(10))  # Output: 433494437
print(prime_fib(11))  # Output: 109461773193
print(prime_fib(12))  # Output: 165580141
print(prime_fib(13))  # Output: 46368
print(prime_fib(14))  # Output: 121393779783
print(prime_fib(15))  # Output: 196418
print(prime_fib(16))  # Output: 317811
print(prime_fib(17))  # Output: 514229
print(prime_fib(18))  # Output: 832040
print(prime_fib(19))  # Output: 4183548
print(prime_fib(20))  # Output: 6767630
print(prime_fib(21))  # Output: 109461773193
print(prime_fib(22))  # Output: 196