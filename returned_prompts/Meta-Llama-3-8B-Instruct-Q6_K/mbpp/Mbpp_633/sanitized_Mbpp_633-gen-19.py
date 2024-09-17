def pair_xor_Sum(lst, n):
    xor_sum = 0
    for i in range(n):
        for j in range(i+1, n):
            xor_sum += lst[i] ^ lst[j]
    return xor_sum