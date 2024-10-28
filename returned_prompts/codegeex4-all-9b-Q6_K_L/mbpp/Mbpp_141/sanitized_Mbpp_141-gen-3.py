def pancake_sort(lst):
    def flip(start, end):
        while start < end:
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1

    n = len(lst)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if lst[j] > lst[max_index]:
                max_index = j
        if max_index != i:
            flip(0, max_index)
            flip(0, i)
    return lst