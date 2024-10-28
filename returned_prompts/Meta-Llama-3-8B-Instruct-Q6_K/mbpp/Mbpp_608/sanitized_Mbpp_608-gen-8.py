def bell_Number(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return sum(bell_Number(i) for i in range(1, n)) + 1