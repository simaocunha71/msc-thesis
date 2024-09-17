```
def sub_list(list1, list2):
    return [a - b for a, b in zip(list1, list2)]
```



The unit test `assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]` ensures that the function correctly subtracts the elements of the two lists. 

The function uses list comprehension and the built-in `zip` function to iterate over the two lists in parallel. The `zip` function returns an iterator of tuples, where each tuple contains one element from each of the input iterables. The list comprehension then subtracts the corresponding elements from each tuple and returns the result as a new list.

For example, `sub_list([1, 2, 3], [4, 5, 6])` would return `[-3, -3, -3]`, which is the result of subtracting the corresponding elements from the two input lists.