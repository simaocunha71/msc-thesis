    if n == 0:
        return [1]
    elif n == 1:
        return [1, 3]
    elif n == 2:
        return [1, 3, 2, 8]
    else:
        sequence = [1, 3]
        for i in range(n - 2):
            sequence.append(sequence[i] + sequence[i - 1] + sequence[i + 1])
        return sequence


