```
def get_Inv_Count(arr):
    if len(arr) <= 1:
        return 0
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left_count = get_Inv_Count(left)
    right_count = get_Inv_Count(right)
    merged_count = merge_count(left, right)
    return left_count + right_count + merged_count

def merge_count(left, right):
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
    merged.extend(left[i:])
    merged.extend(right[j:])
    return inv_count
```
This function uses a divide-and-conquer approach to count the number of inversions in the given array. It first divides the array into two halves, recursively counts the number of inversions in each half, and then merges the two halves while counting the number of inversions that occur during the merge process. The merge process involves comparing elements from the two halves and swapping them if the element from the right half is smaller. The number of inversions during the merge process is calculated as the difference between the length of the left half and the current index, because all the elements from the left half that are greater than the current element from the right half will be swapped during the merge process.

The unit test `assert get_Inv_Count([1,20,6,4,5]) == 5` checks if the function correctly counts the number of inversions in the given array. The array [1,20,6,4,5] has 5 inversions: (20,1), (20,6), (20,4), (6,4), and (6,5). The function should return 5, which is the correct count of inversions.