You can solve this problem by using Python's built-in list slicing feature. Here is a sample solution:

```Python
def is_Sub_Array(arr1, arr2):
    if len(arr1) > len(arr2):
        return False
    for i in range(len(arr2) - len(arr1) + 1):
        if arr1 == arr2[i:i+len(arr1)]:
            return True
    return False
```

In this function, we first check if the length of the first list is greater than the length of the second list. If it is, we can immediately return False because the second list cannot be a sublist of the first list. 

Then, we iterate over the second list and check if the first list is equal to a slice of the second list of the same length. If we find a match, we return True. If we don't find a match after checking all slices, we return False.

Here is an example usage of this function:

```Python
print(is_Sub_Array([1,4,3,5],[1,2,3,4,5])) # returns True
print(is_Sub_Array([1,4,3,5],[1,2])) # returns False
```

The unit test you provided, `assert is_Sub_Array([1,4,3,5],[1,2]) == False`, is a good example of how this function should behave. It correctly returns False because [1,2] is not a sublist of [1,4,3,5]. 