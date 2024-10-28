```
def left_insertion(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
```


The function `left_insertion` takes a sorted array `arr` and a target value `target` as input, and returns the index where the target value should be inserted to maintain the sorted order. 

The function uses binary search to find the insertion point. If the target value is greater than the middle element, it moves the left pointer to the middle index; otherwise, it moves the right pointer to the middle index. The loop continues until the left pointer meets the right pointer. The left pointer at this point is the insertion point. 

For example, if the input array is `[1,2,4,5]` and the target value is `6`, the function will return `4`, which is the index where `6` should be inserted to maintain the sorted order. 

The unit test `assert left_insertion([1,2,4,5],6)==4` ensures that the function works correctly. 





Note: 
The problem doesn't explicitly state whether the array is sorted or not, but the unit test `assert left_insertion([1,2,4,5],6)==4` implies that the array is sorted in ascending order. 

Also, the problem doesn't specify whether the target value is present in the array or not. However, based on the unit test, it seems that the target value is not present in the array and the function should return the index where it should be inserted to maintain the sorted order. 

If the target value is present in the array, the function should return the index of the target value. If the array is not sorted, the function may not work correctly. 

In this implementation, the function assumes that the array is sorted in ascending order. If the array is not sorted, the function will not work correctly. 

The time complexity of this function is O(log n), where n is the length of the array, because it uses binary search. The space complexity is O(1), because it only uses a constant amount of space to store the pointers and the target value. 