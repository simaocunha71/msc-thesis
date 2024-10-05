
def count_up_to(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    primes = []
    for i in range(n):
        if is_prime(i):
            primes.append(i)
    return primes

print(count_up_to(5))  # => [2,3]
print(count_up_to(11))  # => [2,3,5,7]
print(count_up_to(0))  # => []
print(count_up_to(20))  # => [2,3,5,7,11,13,17,19]
print(count_up_to(1))  # => []
print(count_up_to(18))  # => [2,3,5,7,11,13,17]

# Alternate solution using Sieve of Eratosthenes
def count_up_to(n):
    sieve = [0, 0] + [1 for i in range(2, n+1)]
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = 0
    return [x for x in range(2, n) if sieve[x]]

print(count_up_to(5))  # => [2,3]
print(count_up_to(11))  # => [2,3,5,7]
print(count_up_to(0))  # => []
print(count_up_to(20))  # => [2,3,5,7,11,13,17,19]
print(count_up_to(1))  # => []
print(count_up_to(18))  # => [2,3,5,7,11,13,17]

# Time complexity