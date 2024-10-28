def pair_xor_Sum(lst,n):
    total_sum = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            total_sum ^= (lst[i] ^ lst[j])
    return total_sum ^ n