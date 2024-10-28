    def fib_prime(n: int):
        fib_list = [0, 1, 1]
        while len(fib_list) <= n:
            fib_list.append(fib_list[-1] + fib_list[-2])
            if len(fib_list) > 4 and fib_list[-1] % 4 != 0:
                for i in range(3, int(fib_list[-1] ** 0.5) + 1, 2):
                    if fib_list[-1] % i == 0:
                        return False
                return True
        return False

    while True:
        if fib_prime(n):
            return fib_list[n]
        n += 1


