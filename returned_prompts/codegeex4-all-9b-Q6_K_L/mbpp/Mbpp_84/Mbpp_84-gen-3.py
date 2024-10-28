def sequence(n):
    sequence = [1, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence[n - 1]