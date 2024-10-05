def count_up_to(n):
    if n < 2: return []
    primes = [2]
    for i in range(3, n, 2):
        is_prime = True
        for j in primes:
            if i % j == 0:
                is_prime = False
                break
        if is_prime: primes.append(i)
    return primes

# Tests
print(count_up_to(5)) # [2,3]
print(count_up_to(11)) # [2,3,5,7]
print(count_up_to(0)) # []
print(count_up_to(20)) # [2,3,5,7,11,13,17,19]
print(count_up_to(1)) # []
print(count_up_to(18)) # [2,3,5,7,11,13,17]