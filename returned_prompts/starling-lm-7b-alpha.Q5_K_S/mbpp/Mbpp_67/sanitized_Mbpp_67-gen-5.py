def bell_number(n):
    b = [1, 1] + [0] * n
    for i in range(2, n + 1):
        b[i] = sum(b[i - j] for j in range(i)) + 1
    return b[n]