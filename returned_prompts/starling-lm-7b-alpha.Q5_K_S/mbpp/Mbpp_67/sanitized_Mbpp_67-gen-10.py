def bell_number(n):
    B = [1, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        for j in range(i):
            B[i] += B[j] * B[i - 1 - j]
    return B[n]