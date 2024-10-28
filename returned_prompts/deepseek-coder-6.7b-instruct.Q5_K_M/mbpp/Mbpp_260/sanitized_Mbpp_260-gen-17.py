def newman_prime(n):
    prime_numbers = [2, 3, 5, 7, 11, 13]
    if n <= 6:
        return prime_numbers[n - 1]
    i = 14
    while len(prime_numbers) < n:
        is_prime = True
        sqrt_i = int(i ** 0.5)
        for prime in prime_numbers:
            if prime > sqrt_i:
                break
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)
        i += 2
    return prime_numbers[-1]