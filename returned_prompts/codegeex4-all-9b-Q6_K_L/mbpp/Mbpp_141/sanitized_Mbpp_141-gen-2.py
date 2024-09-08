def pancake_sort(lst):
    def flip(arr, k):
        arr[:k] = arr[:k][::-1]

    n = len(lst)
    for i in range(n):
        max_idx = lst.index(max(lst[:n-i]))
        if max_idx != n-i-1:
            flip(lst, max_idx+1)
            flip(lst, n-i)

    return lst