```
def unique_Element(lst):
    return len(set(lst)) == 1
```


Here, we are using the set data structure in Python, which is an unordered collection of unique elements. We convert the list to a set and then check if the length of the set is equal to 1. If it is, then the list contains only one distinct element. Otherwise, it contains more than one distinct element.

The unit test `assert unique_Element([1,1,1]) == True` confirms this, as it checks if a list with all the same elements returns `True`, indicating that there is only one distinct element.