def is_Diff(n):
    str_n = str(n)
    sum1 = 0
    sum2 = 0
    for i in range(len(str_n)):
        if i % 2 == 0:
            sum1 += int(str_n[i])
        else:
            sum2 += int(str_n[i])
    return abs(sum1 - sum2) % 11