def newman_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def newman_sequence(n):
        sequence = [2]
        for i in range(1, n):
            sequence.append(sequence[i - 1] + 1)
        return sequence

    def prime_count(sequence):
        count = 0
        for num in sequence:
            if is_prime(num):
                count += 1
        return count

    sequence = newman_sequence(n + 1)
    while prime_count(sequence) < n:
        sequence.append(sequence[-1] + 1)
    return sequence[n]