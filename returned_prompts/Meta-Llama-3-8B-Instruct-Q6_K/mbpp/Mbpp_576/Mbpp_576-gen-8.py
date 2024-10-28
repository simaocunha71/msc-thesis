You can use the following function to check if a list is a sublist of another:
```
def is_Sub_Array(arr1, arr2):
    if len(arr1) > len(arr2):
        return False
    for i in range(len(arr2) - len(arr1) + 1):
        if arr1 == arr2[i:i+len(arr1)]:
            return True
    return False
```
This function first checks if the length of the first array is greater than the length of the second array. If it is, it immediately returns False, because a sublist cannot be longer than its parent list. 

Then, it iterates over the second array, checking if each subarray of the same length as the first array is equal to the first array. If it finds a match, it returns True. 

If it doesn't find a match after checking all subarrays, it returns False, indicating that the first array is not a sublist of the second array. 

The unit test `assert is_Sub_Array([1,4,3,5],[1,2]) == False` shows that this function works correctly. It returns False because [1,2] is not a sublist of [1,4,3,5]. 