import pytest
from comb_sort import comb_sort
import pytest
from comb_sort import comb_sort
def comb_sort(lst):
    gap = len(lst)
    swapped = True

    while gap > 1 or swapped:
        gap = max(1, int(gap / 1.3))  # minimum gap is 1
        swapped = False
        for i in range(len(lst) - gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swapped = True

    return lst