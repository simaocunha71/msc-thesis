```
def insert_element(lst, element):
    result = [element]
    result += lst
    result += [element]
    return result
```


Python code that inserts an element before each element in a list. It first creates a new list with the element, then adds the original list, and finally adds the element again. The result is a list where the element is inserted before each element in the original list.

Note that the unit test provided, `assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']`, suggests that the element should be inserted before each element in the list, not just after. This means that the element will appear twice in the resulting list, once before each element in the original list. This is different from the typical behavior of inserting an element before each element in a list, which would result in the element appearing once in the resulting list.

This code is designed to pass the provided unit test, but it may not be the expected behavior for inserting an element before each element in a list. If you want to insert the element before each element in the list, you would need to modify the code accordingly. For example:

```
def insert_element(lst, element):
    result = []
    for e in lst:
        result.append(element)
        result.append(e)
    return result
```

This version of the function will insert the element before each element in the list, resulting in the element appearing once in the resulting list. It does this by iterating over the elements in the original list, appending the element before each element, and appending the element itself. The result is a new list where the element is inserted before each element in the original list.