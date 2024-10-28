def comb_sort(my_list):
    n = len(my_list)
    gap = n
    swapped = True

    while gap > 1 or swapped:
        gap = int(gap / 1.247330950103979)
        if gap == 9 or gap == 10:
            gap = 11

        swapped = False

        for i in range(n - gap):
            if my_list[i] > my_list[i + gap]:
                my_list[i], my_list[i + gap] = my_list[i + gap], my_list[i]
                swapped = True

    return my_list