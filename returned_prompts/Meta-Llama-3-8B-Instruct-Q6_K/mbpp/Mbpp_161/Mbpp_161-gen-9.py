```
def remove_elements(lst1, lst2):
    return [i for i in lst1 if i not in lst2]
```
This function uses a list comprehension to create a new list that contains all elements from `lst1` that are not present in `lst2`. The `if i not in lst2` condition filters out the elements that are present in `lst2`. 

For example, if `lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` and `lst2 = [2, 4, 6, 8]`, the function will return `[1, 3, 5, 7, 9, 10]`. 

The unit test `assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]` ensures that the function works correctly. 

The function has a time complexity of O(n*m), where n is the length of `lst1` and m is the length of `lst2`. This is because the function iterates over each element in `lst1` and checks if it is present in `lst2`. If `lst2` is much larger than `lst1`, the function may be slow. However, for most practical purposes, this function should be sufficient. 