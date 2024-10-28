def pancake_sort(lst):
    def flip(i):
        lst[:i+1] = lst[:i+1][::-1]

    for i in range(len(lst) - 1, -1, -1):
        max_index = lst.index(max(lst[:i+1]))
        if max_index != i:
            flip(max_index)
            flip(i)
    return lst