
def bell_Number(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return bell_Number(n - 1) + bell_Number(n - 2)


