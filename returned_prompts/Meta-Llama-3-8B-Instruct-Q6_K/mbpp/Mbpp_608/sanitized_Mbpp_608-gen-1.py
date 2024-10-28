def bell_Number(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return 2 * bell_Number(n - 1) + bell_Number(n - 2)