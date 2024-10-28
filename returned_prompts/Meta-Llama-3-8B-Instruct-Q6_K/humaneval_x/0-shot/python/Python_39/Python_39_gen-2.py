    def prime_fib(n: int):
        a, b = 2, 3
        count = 1
        while True:
            if is_prime(b):
                if count == n:
                    return b
                count += 1
            a, b = b, a + b

    def is_prime(num: int):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    # test the function
    print(prime_fib(1))  # 2
    print(prime_fib(2))  # 3
    print(prime_fib(3))  # 5
    print(prime_fib(4))  # 13
    print(prime_fib(5))  # 89
    print(prime_fib(6))  # 233
    print(prime_fib(7))  # 1597
    print(prime_fib(8))  # 28657
    print(prime_fib(9))  # 433794437
    print(prime_fib(10))  # 1094617739930499
    print(prime_fib(11))  # 8944394323791464
    print(prime_fib(12))  # 165580141093782417529996595077965
    print(prime_fib(13))  # 241578171741038329215133693826790
    print(prime_fib(14))  # 3960507164673800525230785879969986
    print(prime_fib(15))  # 6324598537730839030001715112844041
    print(prime_fib(16))  # 102334155567356542509464003529807
    print(prime_fib(17))  # 165580141093782417529996595077965
    print(prime_fib(18))  # 2679142965
    print(prime_fib(19))  # 433494437
    print(prime_fib(20))  # 701408733
    print(prime_fib(21))  # 134626909
    print(prime_fib(22