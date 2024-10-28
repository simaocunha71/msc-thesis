```
def unique_Element(lst):
    return len(set(lst)) == 1
```







Explanation:
The problem is asking to write a function that takes a list of numbers as input and returns True if the list contains only one distinct element and False otherwise.

The provided unit test `assert unique_Element([1,1,1]) == True` suggests that the function should return True for a list with all identical elements.

To solve this problem, we can convert the list to a set, which removes duplicates. If the length of the set is 1, it means the list had only one distinct element. Therefore, we can return True in this case.

Here's the implementation:
```
def unique_Element(lst):
    return len(set(lst)) == 1
```
This function works by converting the input list `lst` to a set using the `set()` function. The `set()` function removes duplicates, so if the list had more than one distinct element, the set will have more than one element. The `len()` function returns the number of elements in the set. If the length is 1, it means the list had only one distinct element, and the function returns True. Otherwise, it returns False.