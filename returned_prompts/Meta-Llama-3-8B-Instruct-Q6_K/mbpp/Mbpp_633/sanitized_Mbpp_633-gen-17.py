def pair_xor_Sum(lst, k):
    total_xor_sum = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            total_xor_sum += lst[i] ^ lst[j]
    return total_xor_sum ^ k