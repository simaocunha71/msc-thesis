```
def get_Inv_Count(arr):
    n = len(arr)
    if n < 2:
        return 0
    else:
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]
        left_count = get_Inv_Count(left)
        right_count = get_Inv_Count(right)
        merged_count = merge_and_count(left, right)
        return left_count + right_count + merged_count

def merge_and_count(left, right):
    merged = []
    i = j = inv_count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inv_count += len(left) - i
    merged += left[i:]
    merged += right[j:]
    return inv_count
```


This solution is based on the merge sort algorithm with a modification to count the number of inversions. The idea is to divide the array into two halves, recursively count the number of inversions in each half, and then merge the two halves while counting the number of inversions. The merge operation is modified to count the number of inversions by comparing elements from the two halves and incrementing the count whenever an element from the left half is greater than an element from the right half.

The unit test `assert get_Inv_Count([1,20,6,4,5]) == 5` helps to understand the problem better. It is clear that the input array is already sorted, and the function should return the total number of inversions in the array. In this case, the inversions are 5, because there are 5 pairs of elements that are in the wrong order. The function correctly returns this value.