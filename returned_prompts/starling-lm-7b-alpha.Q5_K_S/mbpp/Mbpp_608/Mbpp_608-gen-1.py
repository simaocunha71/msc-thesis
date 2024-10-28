
def bell_Number(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial // (n+1)


