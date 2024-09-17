def bell_Number(n):
    if n == 0:
        return 1
    else:
        return (n + 1) * bell_Number(n - 1) / (n + 1)