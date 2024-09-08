
def get_Inv_Count(arr):
    inv_count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count

print(get_Inv_Count([1,20,6,4,5]))

"""
Explanation:
There are 5 inversions in the array: (20, 6), (20, 4), (20, 5), (6, 4), (6, 5)
"""
<jupyter_output>
5
<jupyter_text>
This algorithm is not efficient for large lists, it has a time complexity of O(n^2). Let's try to improve it using Merge Sort. The inversions in the merge sort process can be counted.
<jupyter_code>
def merge_sort(arr):
    inv_count = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        inv_count += merge_sort(left)
        inv_count += merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
                k += 1
            else:
                arr[k] = right[j]
                j += 1
                k += 1
                inv_count += len(left) - i

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return inv_count

print(merge_sort([1,20,6,4,5]))
<jupyter_output>
5
<jupyter_text>
This version of the algorithm is more efficient and