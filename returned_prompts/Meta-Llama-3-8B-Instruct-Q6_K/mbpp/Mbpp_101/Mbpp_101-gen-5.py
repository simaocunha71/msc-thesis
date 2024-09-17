```
def kth_element(arr, k):
    k -= 1
    arr.sort()
    return arr[k]
```


The unit test `assert kth_element([12,3,5,7,19], 2) == 3` suggests that the array is 1-indexed, so we subtract 1 from the input k to adjust the indexing. Then, we sort the array and return the kth element. This function assumes that 1 <= k <= len(arr). If k is outside this range, the function will raise an IndexError. If the array is empty, the function will raise a ValueError. In practice, you might want to add error handling to deal with these cases.  For example, you could return None if k is out of range, or raise a custom exception if the array is empty.  Here is an updated version of the function with error handling:
```
def kth_element(arr, k):
    k -= 1
    if k < 0 or k >= len(arr):
        return None  # or raise a custom exception
    arr.sort()
    return arr[k]
```


This function returns None if k is out of range, but you could modify it to raise a custom exception instead. For example:
```
class OutOfRangeError(Exception):
    pass

def kth_element(arr, k):
    k -= 1
    if k < 0 or k >= len(arr):
        raise OutOfRangeError(f"k is out of range (1 <= k <= {len(arr)})")
    arr.sort()
    return arr[k]
```


This version of the function raises an OutOfRangeError if k is out of range, with a message that describes the valid range of k.  You could modify the message to suit your needs.  Similarly, you could add error handling for the case where the array is empty.  For example:
```
class EmptyArrayError(Exception):
    pass

def kth_element(arr, k):
    k -= 1
    if not arr:
        raise EmptyArrayError("The array is empty")
    if k < 0 or k >= len(arr):
        raise OutOfRangeError(f"k is out of range (1 <= k <= {len(arr)})")
    arr.sort()
    return arr[k]
```


This version of the function raises an EmptyArrayError if the array is empty, and an OutOfRangeError if k is out of range.  You could modify the