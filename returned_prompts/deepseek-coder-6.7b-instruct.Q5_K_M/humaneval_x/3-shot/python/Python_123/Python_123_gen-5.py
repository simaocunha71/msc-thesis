    collatz_sequence = [n]

    while n != 1:
        if n % 2 != 0:
            collatz_sequence.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1

    return sorted([num for num in collatz_sequence if num % 2 != 0])


