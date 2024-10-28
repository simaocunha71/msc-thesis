def bell_Number(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        bell = [0, 1]
        for i in range(2, n + 1):
            bell.append(sum(bell[i - 1:]))
        return bell[n]