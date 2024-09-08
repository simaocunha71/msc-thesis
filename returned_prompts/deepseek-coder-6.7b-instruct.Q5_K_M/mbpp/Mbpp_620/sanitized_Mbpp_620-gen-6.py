def largest_subset(lst):
    lst.sort()
    n = len(lst)
    T = [1]*n
    for i in range(1, n):
        for j in range(i):
            if lst[i] % lst[j] == 0:
                T[i] = max(T[i], T[j] + 1)
    return max(T)