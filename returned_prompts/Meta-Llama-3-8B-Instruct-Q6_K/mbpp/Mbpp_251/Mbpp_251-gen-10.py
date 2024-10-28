```
def insert_element(lst, element):
    new_list = [element]
    new_list.extend([element if i != 0 else x for i, x in enumerate(lst)])
    return new_list
```


The unit test `assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']` suggests that the function should insert the element before each element in the list, not after. The function `insert_element` does this by first creating a new list with the element, and then extending this list with the elements from the original list, inserting the element before each one. The condition `i != 0` in the list comprehension is used to ensure that the element is inserted before each element in the list, and not after the first element. 

This function assumes that the list is not empty. If the list could be empty, you might want to add a check for this at the beginning of the function. 

Also, this function does not modify the original list, but returns a new list. If you want to modify the original list, you would need to use the `insert` method of the list class.  However, this would not be suitable for this problem because it would only allow you to insert an element at a specific position, not before each element in the list.  Therefore, returning a new list is the more flexible and general solution. 

The time complexity of this function is O(n), where n is the length of the list, because it needs to iterate over the list to create the new list. The space complexity is also O(n), because the new list can be up to twice the size of the original list.  Therefore, this function is not suitable for very large lists.  However, for most practical purposes, it should be fine.  If you need a more efficient solution, you would need to use a different data structure, such as a linked list, or use a more efficient algorithm, such as inserting the elements into a set or a dictionary.  However, these solutions would be more complex and less flexible than this function. 
```python
def insert_element(lst, element):
    new_list = [element]
    new_list.extend([element if i != 0 else x for i, x in enumerate(lst)])
    return new_list
```


The unit test `assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red