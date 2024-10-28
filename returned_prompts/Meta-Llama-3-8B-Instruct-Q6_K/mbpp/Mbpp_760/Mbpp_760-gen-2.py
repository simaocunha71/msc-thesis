```
def unique_Element(lst):
    return len(set(lst)) == 1
```



Explanation:
The problem is asking to write a function that checks if a list of numbers contains only one distinct element. For example, if the list is [1, 1, 1], the function should return True because there is only one distinct element (1) in the list.

We can solve this problem by converting the list to a set, which removes duplicates. If the length of the set is 1, it means that the list contains only one distinct element. Otherwise, it means that the list contains more than one distinct element.

Here is the Python function that implements this solution:

```
def unique_Element(lst):
    return len(set(lst)) == 1
```

This function works because the set data structure in Python automatically removes duplicates. For example, if you create a set from the list [1, 1, 1], the resulting set will be {1}, which has only one element. If you create a set from the list [1, 2, 3], the resulting set will be {1, 2, 3}, which has three elements. By comparing the length of the set to 1, we can determine whether the list contains only one distinct element or not.

The unit test `assert unique_Element([1,1,1]) == True` ensures that the function returns the correct result for the list [1, 1, 1]. This test passes because the function correctly returns True for this list, indicating that it contains only one distinct element.