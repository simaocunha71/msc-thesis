    if n == 1:
        return [3]
    if n == 2:
        return [3, 2]

    seq = [3, 2, 8]
    for i in range(3, n):
        seq.append(seq[-1] + seq[-2] + seq[-3])

    return seq


