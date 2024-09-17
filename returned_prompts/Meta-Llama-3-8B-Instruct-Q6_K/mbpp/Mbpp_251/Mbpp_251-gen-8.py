```
def insert_element(lst, element):
    result = [element]
    for i in lst:
        result.extend([element, i])
    return result
```
This function creates a new list `result` and initializes it with the given element. Then, it iterates over the input list, inserting the element before each element in the list and appending it to the `result` list. The resulting list is then returned. For example, if the input list is `['Red', 'Green', 'Black']` and the element is `'c'`, the function will return `['c', 'Red', 'c', 'Green', 'c', 'Black']`. 