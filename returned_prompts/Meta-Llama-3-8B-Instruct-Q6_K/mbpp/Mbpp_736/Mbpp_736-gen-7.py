```
def left_insertion(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
``` 
The function `left_insertion` is used to find the left insertion point for a specified value in sorted order. It takes a sorted list `arr` and a target value `target` as input. The function uses a binary search approach to find the insertion point. If the target value is found in the list, the function returns the index of the target value. If the target value is not found, the function returns the index where the target value should be inserted to maintain the sorted order. The unit test `assert left_insertion([1,2,4,5],6)==4` ensures that the function correctly identifies the left insertion point for a target value that is not present in the list. 

This problem is a variation of the binary search problem, where instead of finding the target value, we need to find the insertion point. The time complexity of this function is O(log n), where n is the length of the input list. The space complexity is O(1), as it only uses a constant amount of space. 