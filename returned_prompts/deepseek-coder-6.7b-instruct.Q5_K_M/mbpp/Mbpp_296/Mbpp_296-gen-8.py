"""
We can solve this problem by using merge sort algorithm. In merge sort, while merging the two halves, we count the inversions.

Here is the Python code to achieve this:
"""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_inv = merge_sort(arr[:mid])
    right, right_inv = merge_sort(arr[mid:])
    merged, merge_inv = merge(left, right)
    total_inv = left_inv + right_inv + merge_inv

    return merged, total_inv


def merge(left, right):
    merged = []
    inversions = 0
    while left and right:
        if left[0] <= right[0]:
            merged.append(left[0])
            left = left[1:]
        else:
            merged.append(right[0])
            right = right[1:]
            inversions += len(left)
    merged.extend(left if left else right)
    return merged, inversions


def get_Inv_Count(arr):
    _, inversions = merge_sort(arr)
    return inversions


assert get_Inv_Count([1,20,6,4,5]) == 5
"""
The function merge_sort divides the array into two halves, recursively sorts them and then merges them. During the merge, it counts the number of inversions. The function get_Inv_Count is the main function which calls merge_sort and returns the number of inversions.
"""

"""
The time complexity of the merge sort algorithm is O(n log n) and the space complexity is O(n). So, the time complexity of the get_Inv_Count function is also O(n log n).
"""
"""
"""
"""
"""
"""

"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
