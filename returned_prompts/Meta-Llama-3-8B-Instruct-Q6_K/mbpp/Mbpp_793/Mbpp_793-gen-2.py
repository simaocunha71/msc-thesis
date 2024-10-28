```
def last(arr, target):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == target:
            return i
    return -1
```


This function iterates through the array in reverse order, checking if the current element is equal to the target. If it finds a match, it returns the index of that element. If it doesn't find a match, it returns -1. The unit test `assert last([1,2,3],1) == 0` ensures that the function works correctly for the edge case where the target is the first element in the array. The unit test `assert last([1,2,3],2) == 1` ensures that the function works correctly for the edge case where the target is the second element in the array. The unit test `assert last([1,2,3],3) == 2` ensures that the function works correctly for the edge case where the target is the last element in the array. The unit test `assert last([1,2,3],4) == -1` ensures that the function works correctly for the edge case where the target is not in the array. 

This function assumes that the input array is sorted and that the target element exists in the array. If these assumptions are not met, the function may not work correctly. 

This function has a time complexity of O(n), where n is the number of elements in the array, because it has to potentially iterate through the entire array. This is the best time complexity we can achieve for this problem, because we have to at least look at each element in the array once. 

This function has a space complexity of O(1), because it only uses a constant amount of space to store the index and the target element. This is the best space complexity we can achieve for this problem, because we don't need to store any additional information about the array. 





The problem statement does not specify whether the array is sorted in ascending or descending order. However, based on the unit tests provided, it seems that the array is assumed to be sorted in ascending order. If the array is sorted in descending order, the function would need to be modified accordingly.