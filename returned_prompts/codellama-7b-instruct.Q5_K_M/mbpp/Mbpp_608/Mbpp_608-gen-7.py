
def bell_Number(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    if n == 1:
        return 1
    return bell_Number(n - 1) + bell_Number(n - 2)


