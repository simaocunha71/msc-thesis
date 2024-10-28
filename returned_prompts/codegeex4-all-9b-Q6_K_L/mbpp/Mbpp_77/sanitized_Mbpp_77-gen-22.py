def is_Diff(n):
    n = str(n)
    sum1 = 0
    sum2 = 0
    for i in range(0, len(n), 2):
        sum1 += int(n[i])
    for i in range(1, len(n), 2):
        sum2 += int(n[i])
    if abs(sum1 - sum2) % 11 == 0:
        return True
    else:
        return False