```
def remove_elements(lst, to_remove):
    return [i for i in lst if i not in to_remove]
```


The function `remove_elements` takes two lists as input, `lst` and `to_remove`. It returns a new list that contains all elements from `lst` that are not present in `to_remove`. The function uses a list comprehension to iterate over each element `i` in `lst`, and includes `i` in the resulting list only if `i` is not found in `to_remove`. The unit test `assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]` demonstrates the expected behavior of the function. For example, when called with `remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8])`, the function returns the list `[1, 3, 5, 7, 9, 10]`, which is the original list with all elements present in `to_remove` removed. 