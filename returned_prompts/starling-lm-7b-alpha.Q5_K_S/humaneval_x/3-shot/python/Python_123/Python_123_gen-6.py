    collatz = set()

    def collatz_helper(n):
        if n % 2 == 0:
            collatz.add(n)
            collatz_helper(n // 2)
        else:
            collatz.add(n)
            collatz_helper(3 * n + 1)

    collatz_helper(n)

    return sorted(list(collatz))


