"""
def comb_sort(list):
    # Set the swap flag to True
    swapped = True

    # Set the gap to the length of the list divided by 1.3 (rounded down)
    gap = len(list) // 1.3

    # While the gap is greater than 1 and the swap flag is True
    while gap > 1 and swapped:
        # Set the swapped flag to False
        swapped = False

        # Iterate through the list
        for i in range(len(list) - gap):
            # If the current element is greater than the next element, swap them
            if list[i] > list[i + gap]:
                list[i], list[i + gap] = list[i + gap], list[i]
                # Set the swapped flag to True
                swapped = True

        # Divide the gap by 1.3
        gap /= 1.3

    # Return the sorted list
    return list
"""

# Here are some unit tests to check whether your implementation passes all the tests.

def test_comb_sort():
    assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
    assert comb_sort([3, 5, 6, 7, 8, 9]) == [3, 5, 6, 7, 8, 9]
    assert comb_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert comb_sort([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert comb_sort([10, 9, 8, 