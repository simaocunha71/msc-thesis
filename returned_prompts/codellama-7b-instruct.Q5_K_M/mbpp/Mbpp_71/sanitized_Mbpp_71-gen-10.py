def comb_sort(my_list):
    gaps = [70500, 30250, 10500, 3075, 967, 302, 101, 30, 29, 14, 7, 3, 1]
    n = len(my_list)
    gap = gaps[0]
    swaps = 0
    while gap > 1 or swaps < n:
        if gap > 1:
            gap = int(gap / 1.25)
            swaps = 0
        for i in range(n - gap):
            if my_list[i] > my_list[i + gap]:
                my_list[i], my_list[i + gap] = my_list[i + gap], my_list[i]
                swaps = swaps + 1
    return my_list