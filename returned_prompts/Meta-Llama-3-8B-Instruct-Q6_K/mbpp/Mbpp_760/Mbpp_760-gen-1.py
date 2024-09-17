You can solve this problem by using the set data structure in Python. A set in Python is an unordered collection of unique elements.

Here is the Python function that solves the problem:

```python
def unique_Element(lst):
    return len(set(lst)) == 1
```

This function takes a list of numbers as an input, converts it to a set (which removes duplicates), and then checks if the length of the set is equal to 1. If it is, then the function returns True, meaning the list contains only one distinct element. Otherwise, it returns False. 

The unit test `assert unique_Element([1,1,1]) == True` passes because the list [1,1,1] contains only one distinct element, which is 1. The function correctly identifies this and returns True.  If you test the function with a list of different numbers, it will return False. For example, `assert unique_Element([1,2,3]) == False` will return False. 

This function is case-insensitive, meaning it treats 1 and '1' as the same element. If you want to make it case-sensitive, you can convert the list to a set of strings before checking the length. For example, `return len(set(map(str, lst))) == 1`. However, this is not necessary for this problem because the problem statement does not mention anything about case-sensitivity. 