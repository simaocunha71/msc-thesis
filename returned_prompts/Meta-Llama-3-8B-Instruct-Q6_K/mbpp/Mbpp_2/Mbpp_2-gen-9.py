```
def similar_elements(list1, list2):
    return set(list1).intersection(list2)
```


This function uses Python's built-in set data structure to find the common elements between two lists. The set intersection operation is used to find the elements that are present in both sets. The result is a set of unique elements that are present in both input lists.

The unit test `assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))` ensures that the function works correctly. It checks that the function returns the correct set of elements that are common to both input lists.

Note that this function is case-sensitive and considers the order of elements. If you want to ignore the order and case, you can convert the lists to sets and then find the intersection. Here's how you can do it:
```
def similar_elements(list1, list2):
    return set(map(str.lower, list1)).intersection(set(map(str.lower, list2)))
```
This function converts each element in the lists to lowercase using the `map` function and then finds the intersection of the two sets. This way, it ignores the case and order of elements.