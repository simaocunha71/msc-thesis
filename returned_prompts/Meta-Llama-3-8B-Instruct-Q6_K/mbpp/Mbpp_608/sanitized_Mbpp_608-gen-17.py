def bell_Number(n):
    if n == 0:
        return 1
    else:
        return sum(bell_Number(k) * bell_Number(n-k-1) for k in range(n))