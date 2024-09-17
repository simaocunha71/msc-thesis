```
def remove_elements(lst, elements_to_remove):
    return [i for i in lst if i not in elements_to_remove]
```


This function uses a list comprehension to iterate over the elements in the given list. It checks each element to see if it is not present in the list of elements to remove. If the element is not present, it is included in the new list. This effectively removes all elements in the list of elements to remove from the original list. 

The unit test `assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]` demonstrates the function's functionality. It checks that the function correctly removes all elements present in the list `[2, 4, 6, 8]` from the list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`. The result is the expected list `[1, 3, 5, 7, 9, 10]`. 

Note: The time complexity of this function is O(n*m), where n is the length of the list and m is the length of the list of elements to remove. This is because in the worst-case scenario, we need to check each element in the list against each element in the list of elements to remove. 

However, this function is simple and easy to understand, and the time complexity is not a significant issue for most use cases. If you need a more efficient solution, you could consider using a set to store the elements to remove, which would reduce the time complexity to O(n). But this would also make the function more complex. 
```python
def remove_elements(lst, elements_to_remove):
    elements_to_remove_set = set(elements_to_remove)
    return [i for i in lst if i not in elements_to_remove_set]
``` 
This version of the function would have the same output as the original, but it would be more efficient for large inputs. 
```python
def remove_elements(lst, elements_to_remove):
    elements_to_remove_set = set(elements_to_remove)
    return [i for i in lst if i not in elements_to_remove_set]
``` 
The unit test `assert remove_elements([1, 2, 