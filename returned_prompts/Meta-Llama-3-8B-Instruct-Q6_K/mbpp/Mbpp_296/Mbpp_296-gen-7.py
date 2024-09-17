```
def get_Inv_Count(arr):
    inv_count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count
```
This function works by iterating over the array and for each pair of elements, it checks if the first element is greater than the second. If it is, it increments the inversion count. The time complexity of this function is O(n^2), where n is the length of the array. This is because for each element in the array, we are potentially checking every other element.

The unit test provided, `assert get_Inv_Count([1,20,6,4,5]) == 5`, suggests that the function should return 5 for the given array. This is because there are 5 inversions in the array: `(20, 6), (20, 4), (20, 5), (6, 4), (6, 5)`. 

However, it's worth noting that this function has a high time complexity and may not be efficient for large arrays. A more efficient solution would be to use a divide-and-conquer approach, such as the merge sort algorithm, which has a time complexity of O(n log n). 

Here is an example of how you could implement the merge sort algorithm to count inversions:

```
def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, left_inv = merge_sort(arr[:mid])
    right, right_inv = merge_sort(arr[mid:])
    merged, merged_inv = merge(left, right)
    return merged, left_inv + right_inv + merged_inv

def merge(left, right):
    merged = []
    inv_count = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged, inv_count

def get_Inv_Count(arr):
    arr, inv_count = merge_sort(arr)
    return inv_count
```

This function works by recursively dividing the array into smaller