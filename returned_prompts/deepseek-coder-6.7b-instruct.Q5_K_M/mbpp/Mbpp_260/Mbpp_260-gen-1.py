
def newman_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [2]
    num = 3
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 2
    return primes[-1]

print(newman_prime(3))  # 7
assert newman_prime(3) == 7
"""

