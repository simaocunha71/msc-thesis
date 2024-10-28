def bell_number(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    bell_table = [0] * (n + 1)
    bell_table[0] = 1
    bell_table[1] = 1
    for i in range(2, n + 1):
        for j in range(i):
            bell_table[i] += bell_table[j]
    return bell_table[n]