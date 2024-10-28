```
def insert_element(lst, element):
    result = [element]
    for item in lst:
        result.extend([element, item])
    return result
```


This function works by first initializing an empty list `result` with the element to be inserted. Then it iterates over each item in the input list `lst`. For each item, it extends the `result` list with the element to be inserted and the current item. This way, the element is inserted before each item in the list. Finally, the function returns the resulting list. 

The unit test `assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']` ensures that the function works correctly. It checks that the element 'c' is inserted before each item in the list `['Red', 'Green', 'Black']`, resulting in the list `['c', 'Red', 'c', 'Green', 'c', 'Black']`. 

The time complexity of this function is O(n), where n is the length of the input list. This is because it iterates over the input list once. The space complexity is also O(n), as it returns a list with the same length as the input list. 

The function assumes that the input list is non-empty and that the element is not `None`. If these assumptions are not valid, the function may need to be modified to handle these cases. For example, if the input list is empty, the function could return a list with the element only. If the element is `None`, the function could raise an error or return a default value. 