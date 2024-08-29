def count_Pairs(lst,n):
    pairs = 0
    for i in range(n):
        for j in range(i+1,n):
            if lst[i] != lst[j]:
                pairs += 1
    return pairs