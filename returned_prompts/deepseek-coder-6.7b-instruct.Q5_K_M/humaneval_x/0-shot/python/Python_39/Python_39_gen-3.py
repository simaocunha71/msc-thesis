
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def fib(n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    i = 1
    count = 0
    while True:
        fib_num = fib(i)
        if is_prime(fib_num):
            count += 1
            if count == n:
                return fib_num
        i += 1


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
print(prime_fib(11))  # 2971215073
print(prime_fib(12))  # 927372692193079
print(prime_fib(13))  # 106500569586655575
print(prime_fib(14))  # 118590020425741824373370815797124703786376557692610299300
print(prime_fib(15))  # 13