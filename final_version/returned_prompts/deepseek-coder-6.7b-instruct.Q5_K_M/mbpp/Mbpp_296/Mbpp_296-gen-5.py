def get_Inv_Count(arr):
    inversions = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions

print(get_Inv_Count([1,20,6,4,5]))

# In this function, we are iterating over the array and for each element, we are comparing it with all the elements to its right. If the element is greater than the element on its right, then we have found an inversion. We increment the count of inversions by 1. Finally, we return the count of inversions. 
# This function has a time complexity of O(n^2) because for each element, we are iterating over all the elements on its right.

"""
Efficient Solution:
We can use the concept of merge sort to find inversions. In merge sort, while merging two halves, we count the number of inversions.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_inv = merge_sort(arr[:mid])
    right, right_inv = merge_sort(arr[mid:])
    merged, merge_inv = merge(left, right)
    return merged, left_inv + right_inv + merge_inv

def merge(left, right):
    merged = []
    inversions = 0
    while left and right:
        if left[0] <= right[0]:
            merged.append(left[0])
            left = left[1:]
        else:
            merged.append(right[0])
            inversions += len(left)
            right = right[1:]
    merged.extend(left)
    merged.extend(right)
    return merged, inversions

print(merge_sort([1,20,6,4,5]))

# This function has a time complexity of O(n log n) because each merge operation takes O(n) time and we are doing it log(n) times. The space complexity is O(n)