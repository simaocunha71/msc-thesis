def pair_xor_Sum(lst, num):
    res = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            res += lst[i]^lst[j]
    return res