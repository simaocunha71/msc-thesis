```
def sub_list(list1, list2):
    return [a - b for a, b in zip(list1, list2)]
```


The function `sub_list` takes two lists as arguments and returns a new list where each element is the difference between the corresponding elements in the input lists. If the lists are of different lengths, the function will stop when the end of the shorter list is reached. This is because the `zip` function stops iterating when the end of the shorter list is reached.

For example, if we call `sub_list([1, 2, 3], [4, 5, 6])`, the function will return `[-3, -3, -3]`. This is because `1 - 4 = -3`, `2 - 5 = -3`, and `3 - 6 = -3`. If we call `sub_list([1, 2], [4, 5, 6])`, the function will return `[-3, -3]`, because the third element in the second list is not included in the result. 

The unit test `assert sub_list([1, 2, 3],[4,5,6]) == [-3,-3,-3]` ensures that the function behaves as expected. It checks that the function returns the correct result for the given input. If the function returns a different result, the unit test will fail, indicating that the function is not working correctly. 

The function uses list comprehension to create the new list. This is a concise way to create a new list by performing an operation on each element of an existing list. The `zip` function is used to iterate over the elements of the two input lists in parallel. This allows the function to access the corresponding elements of the input lists and calculate the differences. 

The function is designed to be flexible and can be used with lists of any length. It will work correctly for lists of the same length or of different lengths. If the lists are of different lengths, the function will stop when the end of the shorter list is reached. This is because the `zip` function stops iterating when the end of the shorter list is reached. 

The function is also designed to be efficient. It uses list comprehension to create the new list, which is a concise and efficient way to create a new list. The `zip` function is also efficient, as it stops iterating when the end of the shorter list is reached. This means that the function