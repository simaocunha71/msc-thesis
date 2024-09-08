def newman_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_newman_numbers():
        a = [2]
        while True:
            next_num = sum(a[-5:]) + 1
            a.append(next_num)
            yield next_num

    primes = []
    for num in generate_newman_numbers():
        if is_prime(num):
            primes.append(num)
        if len(primes) == n:
            return primes[-1]