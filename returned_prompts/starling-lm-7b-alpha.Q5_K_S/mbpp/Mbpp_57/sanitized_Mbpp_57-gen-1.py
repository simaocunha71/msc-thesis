def find_Max_Num(lst):
    lst.sort()
    l = len(lst)
    max_num = 0
    for i in range(l):
        num = 0
        for j in range(l):
            if i == j:
                continue
            num = num * 10 + lst[j]
        max_num = max(max_num, num)
    return max_num