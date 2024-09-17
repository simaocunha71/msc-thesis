def sequence(n):
    sequence = [0, 1]
    for i in range(2, n+1):
        sequence.append(sequence[sequence[-1]] + sequence[-2])
    return sequence[n]