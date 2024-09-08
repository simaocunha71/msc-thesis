def comb_sort(lst):
    gap = len(lst)
    swapped = True

    while gap > 1 or swapped:
        gap = max(1, int(gap / 1.3))
        swapped = False
        for i in range(len(lst) - gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swapped = True
    return lst

assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""
The comb sort function starts by comparing elements that are a certain distance apart.
If the current element is larger than the next one, it swaps them. The gap between the
elements is initially the length of the list, but is reduced in each iteration,
decreasing the number of comparisons and swaps. The reduction is based on the
1.3 factor, which is a famous constant in computer science. The reduction is performed
until the gap is 1, at which point the function switches to a simple bubble sort for
the final pass.
"""

#2.
