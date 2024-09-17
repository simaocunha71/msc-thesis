```
def get_Inv_Count(arr):
    if len(arr) <= 1:
        return 0
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left_count = get_Inv_Count(left)
    right_count = get_Inv_Count(right)
    merged_count = merge_and_count(left, right)
    return left_count + right_count + merged_count

def merge_and_count(left, right):
    merged = []
    i = j = count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            count += len(left) - i
    merged.extend(left[i:])
    merged.extend(right[j:])
    return count

print(get_Inv_Count([1,20,6,4,5]))
```


The function `get_Inv_Count` recursively splits the array into two halves, counts the inversions in each half and the number of inversions when merging the two halves. It then returns the total count of inversions.

The function `merge_and_count` merges the two sorted halves and counts the number of inversions when merging them. It does this by iterating through the two halves and counting the number of elements in the left half that are greater than the current element in the right half. This is because each such element is an inversion.

The time complexity of this function is O(n log n) due to the recursive splitting and merging of the array. The space complexity is O(n) for the recursive function calls. 





The unit test `assert get_Inv_Count([1,20,6,4,5]) == 5` checks if the function correctly counts the inversions in the given array. The expected output is 5, which is the correct count of inversions in the array.