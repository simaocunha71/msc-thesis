```
def get_Inv_Count(arr):
    n = len(arr)
    if n == 1:
        return 0
    else:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]
        leftInvCount = get_Inv_Count(left)
        rightInvCount = get_Inv_Count(right)
        mergedInvCount = merge_and_count(left, right)
        return leftInvCount + rightInvCount + mergedInvCount

def merge_and_count(left, right):
    merged = []
    invCount = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            invCount += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return invCount
```
This function counts the number of inversions in an array. It does this by recursively dividing the array into two halves until each half contains only one element, then merging the two halves while counting the number of inversions. The merge process involves comparing elements from the two halves and placing the smaller element in the merged array. The number of inversions is counted by incrementing the inversion count whenever an element from the right half is placed before an element from the left half. The total inversion count is the sum of the inversion counts from the recursive calls and the inversions counted during the merge process. The time complexity of this function is O(n log n) and the space complexity is O(n). 

The unit test `assert get_Inv_Count([1,20,6,4,5]) == 5` ensures that the function correctly counts the number of inversions in the given array. 

Note: This function assumes that the input array is a list of integers. If the input array can contain other types of elements, the function may need to be modified accordingly. 