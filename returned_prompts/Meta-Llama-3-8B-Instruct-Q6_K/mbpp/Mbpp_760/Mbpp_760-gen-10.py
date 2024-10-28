```
def unique_Element(lst):
    return len(set(lst)) == 1
```
The function `unique_Element` takes a list of numbers as input and returns a boolean value indicating whether the list contains only one distinct element or not.

The function works by converting the list to a set, which removes duplicates, and then checks if the length of the set is equal to 1. If it is, then the list contains only one distinct element and the function returns `True`. Otherwise, it returns `False`. 

This function passes the given unit test: `assert unique_Element([1,1,1]) == True`. 
```python
print(unique_Element([1,1,1]))  # Output: True
``` 
This function will return `True` for all lists that contain only one distinct element, and `False` for all other lists. 
```python
print(unique_Element([1,2,3]))  # Output: False
print(unique_Element([1,1,1,2,2,2,3,3,3]))  # Output: False
``` 