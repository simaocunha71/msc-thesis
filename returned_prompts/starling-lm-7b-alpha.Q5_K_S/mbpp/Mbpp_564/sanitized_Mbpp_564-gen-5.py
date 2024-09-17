def count_Pairs(l, elem):
    n = len(l)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if l[i] != l[j] and l[i] != elem and l[j] != elem:
                count += 1
    return count