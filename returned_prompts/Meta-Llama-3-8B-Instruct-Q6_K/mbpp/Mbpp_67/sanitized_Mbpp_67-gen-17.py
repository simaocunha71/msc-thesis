def bell_number(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    bell = [0]*(n+1)
    bell[0] = 1
    bell[1] = 1
    for i in range(2, n+1):
        bell[i] = sum(bell[k-1] + bell[k-2] for k in range(1, i+1))
    return bell[n]