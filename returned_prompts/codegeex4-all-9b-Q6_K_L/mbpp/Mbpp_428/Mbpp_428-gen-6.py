def shell_sort(lst):
    length = len(lst)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2
    return lst
