
def bell_number(n):
    bell_num = [0] * (n + 1)
    bell_num[0] = 1
    bell_num[1] = 1
    for i in range(2, n + 1):
        bell_num[i] = bell_num[i - 1] + bell_num[i - 2] + 1
    return bell_num[n]


