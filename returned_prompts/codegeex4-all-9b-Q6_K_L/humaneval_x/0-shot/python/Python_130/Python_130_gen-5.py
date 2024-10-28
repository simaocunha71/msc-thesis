def tri(n):
    if n == 0: return [1]
    if n == 1: return [1, 3]
    if n == 2: return [1, 3, 2]
    sequence = [1, 3, 2]
    for i in range(3, n + 1):
        if i % 2 == 0:
            sequence.append(1 + i / 2)
        else:
            sequence.append(sequence[i - 1] + sequence[i - 2] + sequence[i + 1])
    return sequence

print(tri(3))