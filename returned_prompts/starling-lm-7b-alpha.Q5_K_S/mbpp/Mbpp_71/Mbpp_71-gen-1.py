"""
def comb_sort(arr):
    n = len(arr)
    gap = n
    swapped = True
    while gap != 1 or swapped:
        gap = gap / 1.3
        swapped = False
        for i in range(n):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
    return arr

def test_comb_sort():
    assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]

test_comb_sort()
"""

def comb_sort(arr):
    n = len(arr)
    gap = n
    swapped = True
    while gap != 1 or swapped:
        gap = int(gap / 1.3)
        swapped = False
        for i in range(n):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
    return arr

def test_comb_sort():
    assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]

test_comb_sort()

"""
def comb_sort(arr):
    n = len(arr)
    gap = n
    swapped = True
    while gap != 1 or swapped:
        gap = int(gap / 1.3)
        swapped = False
        for i in range(n):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
    return arr

def test_comb_sort():
    assert comb_sort([5, 15, 37, 25, 79]) == [5