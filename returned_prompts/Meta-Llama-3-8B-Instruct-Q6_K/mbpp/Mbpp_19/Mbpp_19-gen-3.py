```
def test_duplicate(arr):
    return len(arr) != len(set(arr))
```
This function uses the fact that a set in Python is an unordered collection of unique elements. It converts the given array to a set and compares the lengths of the two. If the lengths are different, it means that there were duplicate elements in the array, and the function returns True. If the lengths are the same, it means that there were no duplicate elements, and the function returns False.