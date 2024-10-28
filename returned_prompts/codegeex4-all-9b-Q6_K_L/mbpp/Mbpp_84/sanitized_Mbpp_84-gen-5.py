def sequence(n):
    if n < 1:
        return None
    if n == 1:
        return 1
    sequence = [1, 1]
    for i in range(2, n):
        sequence.append(sequence[sequence[i-1] - 1] + sequence[sequence[i-2] - 1])
    return sequence[n-1]