def bell_number(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        bell = [1, 1]
        for i in range(2, n+1):
            bell.append(sum(bell[i-1:j] for j in range(i, 0, -1)))
        return bell[-1]