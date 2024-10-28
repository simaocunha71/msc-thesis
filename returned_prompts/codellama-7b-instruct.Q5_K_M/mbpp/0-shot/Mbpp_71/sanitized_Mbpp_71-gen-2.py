def comb_sort(my_list):
    n = len(my_list)
    gap = n
    swapped = True
    while gap > 1 or swapped:
        if gap > 1:
            gap = int(gap / 1.247330950103979)
        swapped = False
        for i in range(n - gap):
            if my_list[i] > my_list[i + gap]:
                my_list[i], my_list[i + gap] = my_list[i + gap], my_list[i]
                swapped = True
    return my_list