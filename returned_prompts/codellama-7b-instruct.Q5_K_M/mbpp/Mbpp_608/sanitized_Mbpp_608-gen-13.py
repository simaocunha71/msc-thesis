def bell_Number(n):
    if n == 0:
        return 1
    else:
        return sum(bell_Number(k) for k in range(n))