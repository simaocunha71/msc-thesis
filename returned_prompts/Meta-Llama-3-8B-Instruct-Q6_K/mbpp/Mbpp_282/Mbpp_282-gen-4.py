```
def sub_list(list1, list2):
    return [x - y for x, y in zip(list1, list2)]
```
This function uses list comprehension and the built-in zip function to iterate over the two lists in parallel. The subtraction is done element-wise. For example, if the input lists are [1, 2, 3] and [4, 5, 6], the function will return [-3, -3, -3]. 

The unit test `assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]` ensures that the function works correctly. 

The time complexity of this function is O(n), where n is the length of the shorter list, because it needs to iterate over the lists once. The space complexity is also O(n), because it needs to create a new list with the same length as the input lists. 