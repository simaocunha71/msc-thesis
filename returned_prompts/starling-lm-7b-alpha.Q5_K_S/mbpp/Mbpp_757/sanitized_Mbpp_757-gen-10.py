def count_reverse_pairs(lst):
    lst_rev = []
    for s in lst:
        lst_rev.append(s[::-1])
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst_rev[i] == lst_rev[j]:
                count += 1
    return count