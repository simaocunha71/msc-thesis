
def get_Inv_Count(arr):
    inv_count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count

print(get_Inv_Count([1,20,6,4,5]))

# OR
# Using Merge Sort to count inversions
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    inv_count = 0
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left[0])
            left.pop(0)
        else:
            merged.append(right[0])
            inv_count += len(left)
            right.pop(0)

    while len(left) > 0:
        merged.append(left[0])
        left.pop(0)

    while len(right) > 0:
        merged.append(right[0])
        right.pop(0)

    return merged, inv_count

arr = [1,20,6,4,5]
sorted_arr, inv_count = merge_sort(arr)
print(inv_count)

"""
The first solution works well but it's not efficient for large arrays. The second solution is more efficient because it uses a divide and conquer approach similar to merge sort. It splits the array into two halves, sorts them and then merges them back together. During the merge process, it counts the number of inversions.
"""
<jupyter_output>
5
5
<jupyter_text>
Problem 3
<jupyter_code>
