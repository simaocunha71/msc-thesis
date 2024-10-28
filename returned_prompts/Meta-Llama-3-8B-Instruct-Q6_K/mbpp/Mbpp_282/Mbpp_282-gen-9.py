```
def sub_list(list1, list2):
    return [a - b for a, b in zip(list1, list2)]
```
This function uses list comprehension and the zip function to iterate over the two lists in parallel. For each pair of elements, it subtracts the second element from the first, and returns a new list with the results. The unit test `assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]` ensures that the function works correctly. 
However, this function assumes that the two lists have the same length. If the lists have different lengths, it will stop when the shorter list is exhausted, and the remaining elements in the longer list will be ignored. If you want to handle lists of different lengths, you could use the following function:
```
def sub_list(list1, list2):
    min_len = min(len(list1), len(list2))
    return [a - b for a, b in zip(list1[:min_len], list2[:min_len])]
```
This function finds the length of the shorter list, and then uses list slicing to truncate the longer list to that length. It then subtracts the elements of the two lists element-wise, as before. 
The unit test `assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]` will still pass for this function, because it only tests the case where the lists have the same length. If you want to test the case where the lists have different lengths, you could add additional unit tests. For example:
```
assert sub_list([1, 2, 3, 4],[4,5,6])==[-3,-3,-3]
assert sub_list([1, 2, 3],[4,5,6,7]) == [-3, -3, -3]
assert sub_list([1, 2, 3, 4, 5],[4,5,6]) == [-3, -3, -3]
``` 
These unit tests would ensure that the function works correctly when the lists have different lengths. 
In general, it's a good idea to write unit tests for all of the cases that you expect your function to handle, and to test the function thoroughly before using it in your program. This can help you catch bugs and ensure that your function works correctly in all of the situations that you need it