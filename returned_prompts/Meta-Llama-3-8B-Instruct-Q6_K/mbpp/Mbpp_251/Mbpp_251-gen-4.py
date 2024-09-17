```
def insert_element(lst, element):
    result = []
    for i in lst:
        result.append(element)
        result.append(i)
    return result
```


This function goes through each element in the list and appends the given element before it. The result is a list where the given element is inserted before each element in the original list. 

For example, if the list is ['Red', 'Green', 'Black'] and the element is 'c', the function will return ['c', 'Red', 'c', 'Green', 'c', 'Black']. This is confirmed by the unit test provided. 

The time complexity of this function is O(n), where n is the number of elements in the list, because it needs to iterate over each element in the list. The space complexity is also O(n), because it needs to store each element in the list and the given element for each iteration. 