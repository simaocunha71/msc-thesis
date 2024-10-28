```
def sub_list(list1, list2):
    if len(list1) != len(list2):
        return "Lists are not the same length"
    return [x-y for x, y in zip(list1, list2)]
```


Explanation:
The function `sub_list` takes two lists as input and returns a new list that contains the difference between corresponding elements of the input lists. 

It first checks if the input lists are of the same length. If they are not, it returns an error message. 

If the lists are of the same length, it uses a list comprehension to create the new list. The `zip` function is used to iterate over the input lists in parallel, and the subtraction `x-y` is performed for each pair of elements. 

The result is a new list that contains the element-wise differences of the input lists. 

For example, if the input lists are `[1, 2, 3]` and `[4, 5, 6]`, the function returns `[-3, -3, -3]`. 

The unit test `assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]` verifies that the function works correctly for this specific input. 

The function can be further extended to handle cases where the input lists are not of the same length, or where the elements of the lists are not numbers. However, the current implementation only works for lists of numbers of the same length. 
```python
assert sub_list([1, 2, 3],[4,5,6]) == [-3, -3, -3]
``` 
This test case checks if the function returns the correct result when the input lists are of the same length. 
```python
assert sub_list([1, 2, 3, 4],[4,5,6,7]) == ["Lists are not the same length"]
``` 
This test case checks if the function returns the correct error message when the input lists are of different lengths. 
```python
assert sub_list([1, 2, 3],[4,5]) == ["Lists are not the same length"]
``` 
This test case checks if the function returns the correct error message when the input lists are of different lengths. 
```python
assert sub_list([1, 2, 3],[4,'5',6]) == ["Lists are not the same length"]
``` 
This test case