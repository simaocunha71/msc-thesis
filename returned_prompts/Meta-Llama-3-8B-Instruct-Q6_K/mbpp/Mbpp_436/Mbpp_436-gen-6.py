You can solve this problem with the following function:

```python
def neg_nos(lst):
    return [i for i in lst if i < 0]
``` 

This function uses a list comprehension to iterate over the input list and includes only the elements that are less than 0. The result is a new list containing all the negative numbers from the original list. 

The unit test `assert neg_nos([-1,4,5,-6]) == [-1,-6]` ensures that the function works correctly. It checks if the output of the function is equal to the expected result. If the function returns the correct result, the assertion passes, and if not, it raises an AssertionError. 

You can run the function with different inputs to test it further. For example, `print(neg_nos([-1,4,5,-6,7,8]))` should output `[-1, -6]`. 

This solution has a time complexity of O(n), where n is the number of elements in the input list, because it needs to iterate over all the elements. It has a space complexity of O(m), where m is the number of negative numbers in the input list, because it needs to store all the negative numbers in the output list. 