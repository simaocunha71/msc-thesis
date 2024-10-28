    collatz = []
    while n != 1:
        if n % 2 != 0:
            collatz.append(n)
        n = n // 2 if n % 2 == 0 else n * 3 + 1
    collatz.append(1)
    return sorted(collatz)


