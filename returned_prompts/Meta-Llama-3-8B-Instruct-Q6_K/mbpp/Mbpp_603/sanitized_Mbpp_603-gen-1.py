def get_ludic(n):
    lucid_nums = []
    for i in range(1, n+1):
        if len(set(str(i)))*len(set(int(str(i)) for int_str in set(str(i)))) == len(str(i)):
            lucid_nums.append(i)
    return lucid_nums