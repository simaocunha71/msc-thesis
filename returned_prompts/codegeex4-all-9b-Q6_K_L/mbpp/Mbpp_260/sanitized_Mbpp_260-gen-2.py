def newman_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def newman_shanks_williams_sequence(limit):
        sequence = [2]
        while len(sequence) < limit:
            next_term = sequence[-1] + 1
            sequence.append(next_term)
        return sequence

    primes = []
    for i in range(2, 1000):
        sequence = newman_shanks_williams_sequence(i)
        for num in sequence:
            if is_prime(num) and num not in primes:
                primes.append(num)
                if len(primes) == n:
                    return primes[-1]

    return None