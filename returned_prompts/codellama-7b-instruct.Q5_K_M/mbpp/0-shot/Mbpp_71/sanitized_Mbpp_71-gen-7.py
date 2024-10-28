def comb_sort(my_list):
    gaps = [
        701, 301, 132, 57, 23, 10, 4, 1
    ]
    n = len(my_list)
    gap = gaps[0]
    swapped = True
    i = 0
    while gap > 1 and swapped:
        gap = gaps[i]
        i += 1
        swapped = False
        for j in range(n - gap):
            if my_list[j] > my_list[j + gap]:
                my_list[j], my_list[j + gap] = my_list[j + gap], my_list[j]
                swapped = True
    if not swapped:
        return my_list
    else:
        return comb_sort(my_list)