def sequence(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        sequence = [1, 2]
        for i in range(2, n):
            sequence.append(sequence[sequence[i-2]-1] + sequence[sequence[i-1]-1])
        return sequence[-1]