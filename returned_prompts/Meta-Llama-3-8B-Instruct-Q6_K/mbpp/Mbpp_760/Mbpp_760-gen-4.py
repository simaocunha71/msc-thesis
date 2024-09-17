```
def unique_Element(lst):
    return len(set(lst)) == 1
```
The function `unique_Element` takes a list of numbers as input and returns a boolean value indicating whether the list contains only one distinct element or not. It uses the `set` function to convert the list to a set, which automatically removes any duplicate elements. It then checks if the length of the set is equal to 1, which means that the list contains only one distinct element. If the length of the set is greater than 1, it means that the list contains more than one distinct element. The function returns `True` if the list contains only one distinct element, and `False` otherwise. 

For example, the list `[1,1,1]` contains only one distinct element, so the function returns `True`. The list `[1,2,3]` contains more than one distinct element, so the function returns `False`. 

The unit test `assert unique_Element([1,1,1]) == True` ensures that the function works correctly for this specific case. 

This function assumes that the input list is not empty. If the input list is empty, the function will return `True` because the length of an empty set is 0, which is equal to 1. If you want to handle the case where the input list is empty, you can add a simple check at the beginning of the function. For example: 
```
def unique_Element(lst):
    if not lst:
        return False
    return len(set(lst)) == 1
``` 
This modified function will return `False` if the input list is empty, indicating that the list does not contain only one distinct element. 