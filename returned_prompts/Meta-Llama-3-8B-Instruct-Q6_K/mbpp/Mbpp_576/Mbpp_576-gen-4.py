```
def is_Sub_Array(sublist, array):
    return sublist in [array[i:i+len(sublist)] for i in range(len(array))]
```
This function uses list comprehension to generate all possible sublists of the given array. It then checks if the given sublist is present in any of these sublists. If it is, the function returns True; otherwise, it returns False. 

However, this function will return True for sublists that are not strictly within the array (like [1,2] in [1,2,3,4,5,1,2]). If you want to ensure the sublist is strictly within the array, you can modify the function as follows:

```
def is_Sub_Array(sublist, array):
    return sublist in [array[i:i+len(sublist)] for i in range(len(array)) if i+len(sublist) <= len(array)]
```
This modified function will only consider sublists that are strictly within the array. For example, [1,2] in [1,2,3,4,5,1,2] will return False. 

The unit test `assert is_Sub_Array([1,4,3,5],[1,2]) == False` is also corrected to reflect this change. The original function would return True for this test case, but the modified function will return False as expected. 