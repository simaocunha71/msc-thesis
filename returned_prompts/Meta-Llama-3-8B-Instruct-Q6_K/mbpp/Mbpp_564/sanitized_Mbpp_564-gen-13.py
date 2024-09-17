def count_Pairs(lst, k):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] != lst[j] and lst[i] < k and lst[j] < k:
                count += 1
    return count