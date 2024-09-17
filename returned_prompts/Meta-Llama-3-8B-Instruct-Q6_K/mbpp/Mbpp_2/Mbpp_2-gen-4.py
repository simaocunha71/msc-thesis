```
def similar_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1 & set2
```


The function takes two lists as input and returns a set of elements that are present in both lists. This is achieved by converting the lists to sets and using the set intersection operator (&). The unit test `assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))` ensures that the function works correctly. 

For example, if you call `similar_elements((3, 4, 5, 6),(5, 7, 4, 10))`, the function will return `set((4, 5))`, which means 4 and 5 are the elements that are present in both lists. 

Note that the order of elements in the output set is not guaranteed to be the same as the order in the input lists, as sets are unordered collections. If you need to preserve the order, you can use a list comprehension with an if statement to filter the elements. For example:

```
def similar_elements(list1, list2):
    return [element for element in list1 if element in list2]
```


This function will return a list of elements that are present in both lists, preserving the order of the elements in the first list. However, this approach is less efficient than using sets for large lists, as it requires iterating over the elements of the first list and checking if each element is present in the second list. The set-based approach is more efficient because it uses a hash table to store the elements of the second list, allowing it to look up elements in constant time. 
```python
def similar_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1 & set2
```


This function is more efficient and works correctly for large lists. It converts the input lists to sets and uses the set intersection operator (&) to find the elements that are present in both sets. The result is a set of elements that are present in both lists, which is a more efficient and accurate way to solve the problem. 

The unit test `assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))