def pair_xor_Sum(lst, n):
    total_xor = 0
    for i in range(n):
        for j in range(i+1, n):
            total_xor += lst[i] ^ lst[j]
    return total_xor