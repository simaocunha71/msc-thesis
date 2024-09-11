def largest_subset(lst):
    if not lst:
        return 0
    lst.sort()
    n = len(lst)
    count = 1
    for i in range(1, n):
        if lst[i] % lst[i-1] == 0:
            count += 1
        else:
            break
    return count