    collatz = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        collatz.append(n)

    return sorted([num for num in collatz if num % 2 == 1])


