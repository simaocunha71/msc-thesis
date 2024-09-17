def eulerian_num(n, m):
    if n == 1:
        return 1
    if m == 0:
        return 1
    if m == 1:
        return n
    eulerian = [0] * (n + 1)
    eulerian[1] = 1
    for i in range(2, n + 1):
        eulerian[i] = i * eulerian[i - 1]
        for j in range(1, i):
            eulerian[i] += eulerian[j] * eulerian[i - j - 1]
    return eulerian[n]