def is_Diff(n):
    str_n = str(n)
    sum_odd = sum(int(str_n[i]) for i in range(len(str_n)) if i % 2 == 0)
    sum_even = sum(int(str_n[i]) for i in range(len(str_n)) if i % 2 != 0)
    return abs(sum_odd - sum_even) % 11 == 0

