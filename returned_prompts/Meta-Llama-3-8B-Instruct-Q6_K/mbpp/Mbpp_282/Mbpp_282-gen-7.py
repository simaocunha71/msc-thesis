```
def sub_list(list1, list2):
    return [a - b for a, b in zip(list1, list2)]
```


Explanation:
The function `sub_list` takes two lists as input, `list1` and `list2`. It uses the built-in `zip` function to pair the elements of the two lists together. Then, it uses a list comprehension to subtract each pair of elements and return a new list with the results.

The unit test `assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]` checks that the function correctly subtracts the corresponding elements of the two lists. The expected output is a list with the elements `-3, -3, -3`, which is the result of subtracting `1-4`, `2-5`, and `3-6` from the input lists.