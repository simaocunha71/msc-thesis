```
def similar_elements(list1, list2):
    return set(list1) & set(list2)
```
This function uses the set intersection operation (&) to find the common elements between the two lists. The set function is used to convert the lists to sets, which are unordered collections of unique elements. The intersection of two sets contains all elements that are present in both sets. 

The unit test provided ensures that the function works correctly by comparing the result with the expected output. The test case `similar_elements((3, 4, 5, 6),(5, 7, 4, 10))` checks that the function returns the set `(4, 5)`, which are the common elements in the two lists. 





