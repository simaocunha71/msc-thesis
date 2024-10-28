
def comb_sort(lst):
    gap = len(lst)
    swap = True
    while gap > 1 or swap:
        gap = max(1, int(gap / 1.3))  
        swap = False
        for i in range(len(lst) - gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swap = True
    return lst


