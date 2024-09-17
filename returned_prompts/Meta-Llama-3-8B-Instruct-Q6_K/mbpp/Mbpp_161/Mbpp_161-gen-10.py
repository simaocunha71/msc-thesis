```
def remove_elements(lst1, lst2):
    return [x for x in lst1 if x not in lst2]
```



This function uses a list comprehension to create a new list that includes all elements from `lst1` that are not present in `lst2`. The condition `x not in lst2` is used to filter out the elements that are present in `lst2`. The resulting list is then returned.

For example, if we call `remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8])`, the function will return `[1, 3, 5, 7, 9, 10]`, which are all the elements from the first list that are not present in the second list.  This is in line with the unit test provided, which asserts that the function should behave in this way.  The unit test is:
```
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
```


This function has a time complexity of O(n*m), where n is the length of `lst1` and m is the length of `lst2`, because it needs to iterate over `lst1` and for each element, it needs to check if it is present in `lst2`.  This could be optimized by using a set to keep track of the elements in `lst2`, which would bring the time complexity down to O(n).  However, the current implementation is easy to understand and has a reasonable time complexity for most use cases.