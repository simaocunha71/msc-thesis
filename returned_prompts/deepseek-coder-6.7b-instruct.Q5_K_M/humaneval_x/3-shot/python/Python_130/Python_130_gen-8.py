    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    elif n == 2:
        return [0, 1, 1]
    sequence = [0, 1, 1]
    for i in range(3, n + 1):
        if i % 2 == 0:
            sequence.append(sequence[-1] + sequence[-2])
        else:
            sequence.append(sequence[-2] + sequence[-3] + 1)
    return sequence


