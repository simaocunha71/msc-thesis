def is_Diff(n):
    n = str(n)
    if len(n)%2 == 0:
        return False
    else:
        sum1 = sum(int(n[i]) for i in range(0, len(n), 2))
        sum2 = sum(int(n[i]) for i in range(1, len(n), 2))
        return sum1 == sum2