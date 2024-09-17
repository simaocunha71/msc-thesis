
def comb_sort(list):
    gap = len(list) // 2
    swapped = True
    while gap != 0 and swapped:
        gap = gap // 2
        swapped = False
        for i in range(len(list) - gap):
            if list[i] > list[i + gap]:
                list[i], list[i + gap] = list[i + gap], list[i]
                swapped = True
    return list


