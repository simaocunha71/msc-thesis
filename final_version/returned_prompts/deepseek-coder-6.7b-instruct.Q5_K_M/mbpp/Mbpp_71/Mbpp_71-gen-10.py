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


print(comb_sort([5, 15, 37, 25, 79]))

#tests/test_comb_sort.py
import pytest
from comb_sort import comb_sort


def test_comb_sort():
    assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
    assert comb_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert comb_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert comb_sort([]) == []
    assert comb_sort([1]) == [1]
    assert comb_sort([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert comb_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#tests/test_comb_sort_negative.py
import pytest
from comb_sort import comb_sort


def test_comb_sort_negative():
    with pytest.raises(TypeError):
        comb_sort(None)
    with pytest.raises(TypeError):
       