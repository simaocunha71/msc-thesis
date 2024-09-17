```
def test_duplicate(arr):
    return len(set(arr)) != len(arr)
```


This function converts the given array into a set (which automatically removes any duplicate elements) and then compares the length of the set with the length of the original array. If the lengths are different, it means that the array contained duplicate elements and the function returns True. Otherwise, it returns False. 
The unit test provided, `assert test_duplicate(([1,2,3,4,5]))==False`, suggests that the function should return False for an array without any duplicate elements. 

For example, if we call `test_duplicate([1,2,3,4,5])`, the function will return False because the array does not contain any duplicate elements. If we call `test_duplicate([1,2,2,3,4])`, the function will return True because the array contains duplicate elements. 





```
print(test_duplicate([1,2,3,4,5])) # Expected output: False
print(test_duplicate([1,2,2,3,4])) # Expected output: True
```


The output will be:

```
False
True
```


The function works correctly and passes the unit test.