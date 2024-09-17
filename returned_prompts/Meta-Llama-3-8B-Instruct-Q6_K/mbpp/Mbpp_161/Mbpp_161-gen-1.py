```
def remove_elements(lst1, lst2):
    return [i for i in lst1 if i not in lst2]
```


The function `remove_elements` takes two lists `lst1` and `lst2` as arguments. It uses a list comprehension to create a new list that includes all elements from `lst1` that are not present in `lst2`. This is achieved by iterating over each element `i` in `lst1` and including it in the new list only if `i` is not in `lst2`. The result is a new list with all elements from `lst1` that are not present in `lst2`. 

For example, if we call `remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8])`, the function will return `[1, 3, 5, 7, 9, 10]`. This is because the numbers 2, 4, 6, and 8 are present in both lists and are removed from the result, leaving only the numbers that are unique to `lst1`. 

The unit test `assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]` ensures that the function behaves as expected in this scenario. 
```python
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
```  ```python
def remove_elements(lst1, lst2):
    return [i for i in lst1 if i not in lst2]
```  ```python
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
```  ```python
assert remove_elements([], [1