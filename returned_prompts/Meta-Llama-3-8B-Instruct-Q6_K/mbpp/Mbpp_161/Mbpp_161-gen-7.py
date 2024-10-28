```
def remove_elements(lst1, lst2):
    return [x for x in lst1 if x not in lst2]
```


This function uses list comprehension to create a new list that includes all elements from the original list (`lst1`) that are not present in the second list (`lst2`). The `if x not in lst2` condition in the list comprehension ensures that only elements not in `lst2` are included in the new list. 

For example, if `lst1` is `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` and `lst2` is `[2, 4, 6, 8]`, the function returns `[1, 3, 5, 7, 9, 10]`. 

This function assumes that the input lists do not contain duplicate elements. If the input lists can contain duplicates and you want to remove all occurrences of elements in `lst2` from `lst1`, you can modify the function as follows:

```
def remove_elements(lst1, lst2):
    return [x for x in lst1 if x not in lst2]
```

This modified function uses the `in` operator to check if an element `x` is present in `lst2`, and includes `x` in the new list only if it is not present in `lst2`. This ensures that all occurrences of elements in `lst2` are removed from `lst1`. 

For example, if `lst1` is `[1, 2, 2, 3, 4, 4, 5, 6, 6, 8, 9, 10]` and `lst2` is `[2, 4, 6, 8]`, the function returns `[1, 3, 5, 9, 10]`. 

This function is efficient because it uses a list comprehension to create the new list, which has a time complexity of O(n), where n is the length of `lst1`. The `in` operator has a time complexity of O(m), where m is the length of `lst2`, and it is used in the list comprehension. Therefore, the overall time complexity of the function is O(n*m). 

However, if the input lists are very large, you may want to consider using a more efficient data structure, such as a set, to