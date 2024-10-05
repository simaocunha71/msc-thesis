
def count_up_to(n):
    if n < 2:
        return []
    primes = []
    for possible_prime in range(2, n):
        is_prime = True
        for num in range(2, possible_prime):
            if possible_prime % num == 0:
                is_prime = False
        if is_prime:
            primes.append(possible_prime)
    return primes

print(count_up_to(5)) # [2, 3]
print(count_up_to(11)) # [2, 3, 5, 7]
print(count_up_to(0)) # []
print(count_up_to(20)) # [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(1)) # []
print(count_up_to(18)) # [2, 3, 5, 7, 11, 13, 17]

# Solution 2

def count_up_to(n):
    if n < 2:
        return []
    primes = []
    for possible_prime in range(2, n):
        is_prime = True
        for num in range(2, int(possible_prime ** 0.5) + 1):
            if possible_prime % num == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(possible_prime)
    return primes

print(count_up_to(5)) # [2, 3]
print(count_up_to(11)) # [2, 3, 5, 7]
print(count_up_to(0)) # []
print(count_up_to(20)) # [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(1)) # []
print(count_up_to(18)) # [2, 3, 5, 7, 11, 