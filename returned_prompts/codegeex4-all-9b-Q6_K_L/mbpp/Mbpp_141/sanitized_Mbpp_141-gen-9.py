def pancake_sort(lst):
    def flip(end):
        for i in range(end // 2):
            lst[i], lst[end - i - 1] = lst[end - i - 1], lst[i]

    for end in range(len(lst) - 1, 0, -1):
        if lst[end] > lst[end - 1]:
            flip(end)
            flip(end - 1)
    return lst