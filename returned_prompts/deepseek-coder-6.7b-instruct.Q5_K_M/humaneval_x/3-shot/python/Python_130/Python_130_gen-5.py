    if n == 0:
        return [3]
    elif n == 1:
        return [1, 3]
    elif n == 2:
        return [1, 3, 2]

    sequence = [1, 3, 2]
    for i in range(3, n + 1):
        if i % 2 == 0:
            sequence.append(sequence[-1] + 1)
        else:
            sequence.append(sequence[-1] + sequence[-2] + sequence[-3])
    return sequence


