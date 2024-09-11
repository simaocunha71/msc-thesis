"""
def comb_sort(lst):
    n = len(lst)
    gap = n
    swapped = True
    while gap != 1 or swapped:
        gap = gap / 1.3
        swapped = False
        for i in range(n - gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swapped = True
    return lst

def test_comb_sort():
    assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
    print("All Tests Passed")

if __name__ == "__main__":
    test_comb_sort()
"""

def comb_sort(lst):
    n = len(lst)
    gap = n
    swapped = True
    while gap != 1 or swapped:
        gap = gap / 1.3
        swapped = False
        for i in range(n - gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swapped = True
    return lst

def test_comb_sort():
    assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
    print("All Tests Passed")

if __name__ == "__main__":
    test_comb_sort()





def comb_sort(lst):
    n = len(lst)
    gap = n
    swapped = True
    while gap != 1 or swapped:
        gap = gap / 1.3
        swapped = False
        for i in range(n - gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] =