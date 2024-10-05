def get_odd_collatz(n):
    collatz_sequence = [n]
    while collatz_sequence[-1] != 1:
        if collatz_sequence[-1] % 2 == 0:
            collatz_sequence.append(collatz_sequence[-1] // 2)
        else:
            collatz_sequence.append(3 * collatz_sequence[-1] + 1)
    return sorted([x for x in collatz_sequence if x % 2 != 0])