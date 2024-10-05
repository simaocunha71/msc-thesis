    def collatz(n):
        sequence = [n]
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            sequence.append(n)
        return sequence

    sequence = collatz(n)
    return sorted([x for x in sequence if x % 2 != 0])  # Filter odd numbers and sort them


