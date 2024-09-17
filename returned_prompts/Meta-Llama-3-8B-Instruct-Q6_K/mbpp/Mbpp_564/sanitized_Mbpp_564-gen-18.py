def count_Pairs(lst, k):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] != lst[j] and (lst[i] + lst[j]) % k != 0:
                count += 1
    return count