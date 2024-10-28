def pair_xor_Sum(lst, n):
    lst.sort()
    sum_xor = 0
    for i in range(n):
        sum_xor += lst[i] ^ lst[n - i - 1]
    return sum_xor