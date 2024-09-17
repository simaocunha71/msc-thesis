def comb_sort(my_list):
    shrink = 1.25
    gap = len(my_list)
    swaps = 0
    sorted = False
    while gap > 1 or not sorted:
        gap = int(gap / shrink)
        for i in range(len(my_list) - gap):
            if my_list[i] > my_list[i + gap]:
                my_list[i], my_list[i + gap] = my_list[i + gap], my_list[i]
                swaps += 1
                sorted = False
            else:
                sorted = True
    return my_list