def count_Pairs(l: list, n: int) -> int:
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if l[i] != l[j]:
                count += 1
    return count