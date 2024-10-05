    collatz_sequence = [n]
    while n != 1:
        if n % 2 != 0:
            collatz_sequence.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1

    return sorted(list(set([n for n in collatz_sequence if n % 2 != 0])))


