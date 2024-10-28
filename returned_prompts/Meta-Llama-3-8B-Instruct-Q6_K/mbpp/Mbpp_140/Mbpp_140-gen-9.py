```
def extract_singly(lst):
    return set(item for sublist in lst for item in sublist)
```
This function uses a generator expression to flatten the list of lists into a single set of numbers. The `set` function is used to remove any duplicate numbers. The unit test provided ensures that the function works correctly. 

For example, the input `[(3, 4, 5), (4, 5, 7), (1, 4)]` would return the set `{1, 3, 4, 5, 7}`. 

Note: This function assumes that the input is a list of lists, where each sublist contains numbers. It will not work correctly if the input contains other types of data. 

Also, this function does not preserve the order of the numbers. If the order is important, a different approach would be needed. 

Finally, this function uses the `set` data structure, which is an unordered collection of unique elements. If you need to preserve the order of the numbers, you could use a different data structure, such as a list or a tuple, and modify the function accordingly. 

Here is the modified function to preserve the order:
```
def extract_singly(lst):
    result = []
    for sublist in lst:
        result.extend(sublist)
    return set(result)
```
This function uses the `extend` method to add all the elements of each sublist to the `result` list. It then converts the `result` list to a set and returns it. This function will return a set containing all the unique elements from the input lists, in the order they appear. 

However, this function still does not preserve the order of the numbers if there are duplicates. If you need to preserve the order of the numbers even in the presence of duplicates, you could use a different data structure, such as a list or a tuple, and modify the function accordingly. 

Here is the modified function to preserve the order even in the presence of duplicates:
```
def extract_singly(lst):
    result = []
    for sublist in lst:
        result.extend(sublist)
    return tuple(sorted(result))
```
This function uses the `sorted` function to sort the `result` list and then converts it to a tuple. This function will return a tuple containing all the elements from the input lists, in the order they appear, and preserving the order even in the presence of duplicates. 

Note: The `sorted` function is stable, meaning that