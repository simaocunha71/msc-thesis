    collatz = [n]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        collatz.append(n)

    odd_collatz = [x for x in collatz if x % 2 != 0]

    return sorted(odd_collatz)