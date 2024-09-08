def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
"""
In the above function, we start with a big gap, such as half the length of the array. Then we reduce the gap by half in each iteration until the gap is 1. For each iteration, we start comparing elements that are gap away. If the element at the higher index is smaller than the element at the lower index, we swap them. This way, we gradually sort elements at larger and larger intervals.
"""

# Time Complexity: O(n^2) in the worst case scenario, O(n log n) in the best case scenario.
# Space Complexity: O(1) because it's an in-place sorting algorithm.
<jupyter_output>
<empty_output>
<jupyter_text>
4. Merge Sort
<jupyter_code>
