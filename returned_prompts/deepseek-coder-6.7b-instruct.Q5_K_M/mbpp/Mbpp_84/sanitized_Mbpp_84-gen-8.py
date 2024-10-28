def sequence(n):
    if n == 1 or n == 2:
        return 1
    seq = [0, 1, 1]
    for i in range(3, n + 1):
        seq.append(seq[seq[i - 1]] + seq[i - seq[i - 2]])
    return seq[n]