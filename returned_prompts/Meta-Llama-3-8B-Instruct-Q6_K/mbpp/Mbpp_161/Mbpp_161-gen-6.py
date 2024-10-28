```
def remove_elements(lst1, lst2):
    return [value for value in lst1 if value not in lst2]
```
This function uses a list comprehension to create a new list that includes only the elements from `lst1` that are not present in `lst2`. It does this by iterating over each value in `lst1` and checking if it is not in `lst2`. If it is not in `lst2`, it is included in the new list. The result is a list with all elements from `lst1` that are not present in `lst2`. 

For example, if `lst1` is `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` and `lst2` is `[2, 4, 6, 8]`, the function will return `[1, 3, 5, 7, 9, 10]`, which are all the elements from `lst1` that are not in `lst2`. 

This function assumes that the input lists are lists of hashable objects, such as integers or strings. If the input lists can contain unhashable objects, such as lists or dictionaries, you will need to use a different approach. 

The unit test `assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]` ensures that the function works correctly for this specific input.  It checks that the output of the function is equal to the expected output `[1, 3, 5, 7, 9, 10]`.  If the function works correctly, this test will pass. If the function does not work correctly, this test will fail.  This can help you to identify and fix errors in the function.  You can add more unit tests to ensure that the function works correctly for different inputs.  For example, you could add a test to check that the function works correctly when the input lists are empty.  You could add a test to check that the function works correctly when the input lists are the same.  You could add a test to check that the function works correctly when the input lists are lists of different types of objects. 