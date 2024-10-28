```
def test_duplicate(lst):
    return len(lst) != len(set(lst))
```
The function `test_duplicate` takes an array of integers as input and returns `True` if the array contains any duplicate element and `False` otherwise.

The function works by comparing the length of the input array with the length of a set created from the array. In Python, a set is an unordered collection of unique elements, so if the array contains any duplicate elements, the set will have one fewer element than the array. The function returns `True` if the lengths are different, indicating the presence of a duplicate element, and `False` otherwise.

For example, the test case `test_duplicate(([1,2,3,4,5]))` will return `False` because the array does not contain any duplicate elements. The array has 5 unique elements, and the set created from the array will also have 5 unique elements, so the lengths will be equal, and the function will return `False`. On the other hand, if the array contains any duplicate elements, the function will return `True`. For example, the test case `test_duplicate(([1,2,2,3,4]))` will return `True` because the array contains a duplicate element (the number 2 appears twice). The array has 5 elements, but the set created from the array will have only 4 unique elements, so the lengths will be different, and the function will return `True`. 