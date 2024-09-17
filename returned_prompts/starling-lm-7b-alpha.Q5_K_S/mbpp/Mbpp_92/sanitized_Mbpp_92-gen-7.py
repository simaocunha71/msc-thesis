def is_undulating(num):
    num = str(num)
    return num[0] != num[-1] and all(num[i] != num[i+1] for i in range(len(num)-1))