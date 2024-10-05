    if n <= 1:
        return []

    odd_collatz = []
    while n != 1:
        if n % 2 != 0:
            odd_collatz.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1

    odd_collatz.append(1)
    odd_collatz.sort()

    return odd_collatz

