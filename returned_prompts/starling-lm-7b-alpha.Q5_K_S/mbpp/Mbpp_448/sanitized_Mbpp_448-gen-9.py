def cal_sum(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    s = 0
    for i in range(n):
        s += sum(range(i+1))
    return s + int(str(s)[-2:])