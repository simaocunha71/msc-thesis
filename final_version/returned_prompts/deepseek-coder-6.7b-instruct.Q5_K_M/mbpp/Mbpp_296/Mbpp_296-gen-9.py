def get_Inv_Count(arr):
    inv_count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv_count += 1

    return inv_count


print(get_Inv_Count([1, 20, 6, 4, 5]))


"""
The above function works by comparing each element in the array with all the elements to its right. If it finds an element smaller than the current one, it increments the inversion count. The time complexity of this function is O(n^2), where n is the length of the array.
"""

"""
In python, the above solution can be optimized using merge sort. Merge sort divides the array into two halves, sorts them and then merges them. While merging, it counts the inversions. This approach has a time complexity of O(n log n). Here is the python code for the same:
"""


def merge_sort(arr):
    inv_count = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        inv_count += merge_sort(left_half)
        inv_count += merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
                inv_count += len(left_half) - i
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return inv_count


print(merge_sort