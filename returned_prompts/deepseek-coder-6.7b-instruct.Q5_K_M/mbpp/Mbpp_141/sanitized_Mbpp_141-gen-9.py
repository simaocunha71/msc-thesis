def pancake_sort(lst):
    n = len(lst)
    for i in range(n):
        max_idx = max(0, lst[n-i-1:])
        if max_idx != n-i-1:
            lst[max_idx], lst[n-i-1] = lst[n-i-1], lst[max_idx]
            lst[:n-i] = lst[n-i-1:0:-1] + lst[:n-i-1]
    return lst