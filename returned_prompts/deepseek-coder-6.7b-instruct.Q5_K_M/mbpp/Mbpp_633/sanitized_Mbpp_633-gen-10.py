def pair_xor_Sum(lst: list, n: int) -> int:
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            res += lst[i] ^ lst[j]
    return res * 2