"""
def comb_sort(elements):
    """Sort a list of elements using the comb sort algorithm."""
    swapped = True
    gap = len(elements)
    while gap > 1 or swapped:
        gap = max(1, int(gap / 1.3))
        swapped = False
        for i in range(len(elements) - gap):
            if elements[i] > elements[i + gap]:
                elements[i], elements[i + gap] = elements[i + gap], elements[i]
                swapped = True
    return elements


def test_comb_sort():
    assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]


test_comb_sort()
"""

def comb_sort(elements):
    """Sort a list of elements using the comb sort algorithm."""
    swapped = True
    gap = len(elements)
    while gap > 1 or swapped:
        gap = max(1, int(gap / 1.3))
        swapped = False
        for i in range(len(elements) - gap):
            if elements[i] > elements[i + gap]:
                elements[i], elements[i + gap] = elements[i + gap], elements[i]
                swapped = True
    return elements

def test_comb_sort():
    assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]

test_comb_sort()

# This function uses the comb sort algorithm to sort a list of elements.
# The comb sort algorithm works by repeatedly swapping adjacent elements
# that are out of order until the entire list is sorted. The gap variable
# keeps track of the distance between the elements being compared, and is
# gradually reduced until it becomes 1. The swapped variable keeps track
# of whether any swaps were made during a pass through the list, and is used
# to determine when the list is sorted.

# The test_comb