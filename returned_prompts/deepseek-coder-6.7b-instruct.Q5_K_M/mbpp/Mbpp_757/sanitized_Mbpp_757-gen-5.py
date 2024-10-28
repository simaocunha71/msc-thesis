def count_reverse_pairs(lst):
    count = 0
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] == lst[j][::-1]:
                count += 1
    return count