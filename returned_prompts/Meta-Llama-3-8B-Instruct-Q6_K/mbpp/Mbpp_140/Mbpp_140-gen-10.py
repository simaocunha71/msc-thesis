```
def extract_singly(nested_list):
    result = set()
    for lst in nested_list:
        result.update(lst)
    return result
```
This function takes a list of lists as input, and returns a set of unique numbers. It does this by iterating over each list in the input, and adding each element to the result set. The `update` method is used to add the elements from each list to the set. This has the effect of removing any duplicates, since sets in Python cannot contain duplicate elements. The result is a set of unique numbers, which is returned at the end of the function. 

The unit test provided ensures that the function works correctly. It checks that the function returns the set `{1, 3, 4, 5, 7}` when given the input `[(3, 4, 5), (4, 5, 7), (1, 4)]`. This shows that the function correctly flattens the list of lists into a single set of numbers, and removes any duplicates. 





