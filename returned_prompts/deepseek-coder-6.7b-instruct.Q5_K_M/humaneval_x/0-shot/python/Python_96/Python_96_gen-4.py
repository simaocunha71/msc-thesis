
def count_up_to(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes

print(count_up_to(5))
print(count_up_to(11))
print(count_up_to(0))
print(count_up_to(20))
print(count_up_to(1))
print(count_up_to(18))


