def largest_subset(lst):
    n = len(lst)
    lst.sort()
    subset = [lst[0]]
    for i in range(1, n):
        if lst[i] % lst[i-1] != 0:
            subset.append(lst[i])
    return len(subset)