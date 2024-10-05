    if n == 0:
        return [0]
    elif n == 1:
        return [0, 3]
    elif n == 2:
        return [0, 3, 2]

    sequence = [0, 3, 2]
    for i in range(3, n + 1):
        if i % 2 == 0:
            sequence.append(2)
        else:
            sequence.append(sequence[-1] + sequence[-2] + sequence[-3])

    return sequence


