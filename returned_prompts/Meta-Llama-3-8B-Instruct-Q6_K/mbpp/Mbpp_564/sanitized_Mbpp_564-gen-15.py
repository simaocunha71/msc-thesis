def count_Pairs(lst, k):
    pairs = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] != lst[j]:
                pairs += 1
            if pairs == k:
                return i+1
    return i+1