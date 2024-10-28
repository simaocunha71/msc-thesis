
def bell_Number(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return bell_Number(n-1) + bell_Number(n-2)


