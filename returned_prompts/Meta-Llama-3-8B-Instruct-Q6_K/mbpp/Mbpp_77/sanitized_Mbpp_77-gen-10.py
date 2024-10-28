def is_Diff(n):
    s = str(n)
    s = [int(i) for i in s]
    sum1 = 0
    sum2 = 0
    for i in range(len(s)):
        if i % 2 == 0:
            sum1 += s[i]
        else:
            sum2 += s[i]
    if abs(sum1 - sum2) % 11 == 0:
        return True
    else:
        return False