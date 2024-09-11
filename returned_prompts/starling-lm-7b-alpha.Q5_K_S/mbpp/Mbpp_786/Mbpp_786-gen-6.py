"""
def right_insertion(l, k):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == k:
            return mid
        elif l[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return low
"""

def right_insertion(l, k):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == k:
            return mid
        elif l[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return low


def test_right_insertion():
    assert right_insertion([1, 2, 3], 1) == 0
    assert right_insertion([1, 2, 4, 5], 6) == 4
    assert right_insertion([1, 2, 4, 5], 3) == 2
    assert right_insertion([], 1) == 0
    assert right_insertion([10, 20, 30, 40, 50], 31) == 5
    print("All tests passed.")


test_right_insertion()








"""
Here's the solution to your question:

To locate the right insertion point for a specified value in sorted order, you can use a binary search algorithm. The binary search algorithm works by repeatedly dividing the search interval in half. At each step, the algorithm compares the middle element of the interval to the target value. If the middle element is equal to the target value, the algorithm returns the index of the middle element. If the middle element is greater than the target value, the algorithm continues the search in the lower half of the interval. If the middle element is less than the target value, the algorithm continues the search in the upper half of the interval.

In the given implementation of the binary search algorithm, the function `right_insertion`