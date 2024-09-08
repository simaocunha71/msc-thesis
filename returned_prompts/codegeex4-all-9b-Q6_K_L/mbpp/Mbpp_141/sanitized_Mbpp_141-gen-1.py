def pancake_sort(lst):
    def flip(start, end):
        while start < end:
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1

    n = len(lst)
    for i in range(n - 1, 0, -1):
        max_idx = lst.index(max(lst[:i + 1]))
        if max_idx != i:
            flip(0, max_idx)
            flip(0, i)
    return lst