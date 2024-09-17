def sequence(n):
    sequence = [1, 2]
    for i in range(2, n):
        sequence.append(len(set(sequence[sequence[i-1]:sequence[i]])))
    return sequence[n-1]