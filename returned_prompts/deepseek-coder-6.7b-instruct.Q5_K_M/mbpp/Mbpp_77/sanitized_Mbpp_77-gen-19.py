def is_Diff(n):
    str_n = str(n)
    sum_diff = sum([int(str_n[i]) - int(str_n[i-1]) for i in range(1, len(str_n))])
    return sum_diff % 11 == 0