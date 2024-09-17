
def bell_number(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 1
    return bell_number(n-1) + bell_number(n-2)


