def pair_xor_Sum(lst, n):
    total_sum = 0
    for i in range(n):
        for j in range(i+1, n):
            total_sum += lst[i] ^ lst[j]
    return total_sum