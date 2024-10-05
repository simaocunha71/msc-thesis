    def prime_fib(n: int):
        a, b = 0, 1
        count = 0
        while True:
            a, b = b, a + b
            if is_prime(b):
                count += 1
                if count == n:
                    return b

    def is_prime(num: int):
        """
        is_prime returns True if num is a prime number, False otherwise.
        """
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    pass
# 2,3,5,13,89,233,1597,28657,514229,  # test cases
# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,  # test cases
# print(prime_fib(10))  # 89
# print(prime_fib(20))  # 6765
# print(prime_fib(30))  # 832040
# print(prime_fib(40))  # 433494437
# print(prime_fib(50))  # 12586269025
# print(prime_fib(60))  # 24157817009
# print(prime_fib(70))  # 12166500624
# print(prime_fib(80))  # 498454011879264
# print(prime_fib(90))  # 1548008755920
# print(prime_fib(100))  # 434665576869374564356885276750406257
# print(prime_fib(110))  # 109461773993115813494423144444
# print(prime_fib(120))  # 196418
# print(prime_fib(130))  # 317811106993902443893443066454
# print(prime_fib(140))  # 514229
# print(prime_fib(150))  # 832040
# print(prime_fib(160))  # 12166500624
# print(prime_fib(170))  # 196418
# print(prime_fib(180))