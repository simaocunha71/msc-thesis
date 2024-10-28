def eulerian_num(n, m):
    if m > n:
        return 0
    if m == 0:
        return 1
    eulerian = [0] * (n + 1)
    eulerian[0] = 1
    for i in range(1, n + 1):
        eulerian[i] = i * (eulerian[i - 1] + eulerian[i - 1])
    return eulerian[n] // (m + 1)