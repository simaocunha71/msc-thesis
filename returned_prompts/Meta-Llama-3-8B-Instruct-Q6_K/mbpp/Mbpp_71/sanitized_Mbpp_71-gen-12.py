def comb_sort(lst):
    def comb_sort_step(lst):
        gap = len(lst)
        swapped = True
        while gap > 1 or swapped:
            gap = int(gap / 1.3)
            if gap < 1:
                gap = 1
            swapped = False
            for i in range(len(lst) - gap):
                if lst[i] > lst[i + gap]:
                    lst[i], lst[i + gap] = lst[i + gap], lst[i]
                    swapped = True
        return lst

    return comb_sort_step(lst)