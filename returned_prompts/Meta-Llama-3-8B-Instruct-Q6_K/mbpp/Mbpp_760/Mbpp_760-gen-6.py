You can use a set to remove duplicates and then check the length of the set. If the length is 1, then the list contains only one distinct element.

Here is the python function:
```
def unique_Element(lst):
    return len(set(lst)) == 1
```
This function works by converting the input list to a set, which removes any duplicate elements. It then checks if the length of the set is 1. If it is, then the original list contained only one distinct element. If the length of the set is more than 1, then the list contained more than one distinct element.

The unit test `assert unique_Element([1,1,1]) == True` suggests that the function should return True if the list contains only one distinct element. In this case, the function will return True because the list [1,1,1] contains only one distinct element, which is 1. If the list contained more than one distinct element, the function would return False.