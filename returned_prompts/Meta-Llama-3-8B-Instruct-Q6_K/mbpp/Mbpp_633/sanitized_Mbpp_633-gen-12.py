def pair_xor_Sum(lst, k):
    result = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            result += lst[i] ^ lst[j]
    return result ^ k