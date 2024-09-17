The task is to write a Python function that takes a string as an input and checks whether all the characters in the string are the same or not.

The given unit test `assert all_Characters_Same("python") == False` suggests that the function should return `False` when all characters in the string are not the same. 

Here's the Python function that accomplishes this:

```python
def all_Characters_Same(s):
    return len(set(s)) == 1
```

This function works by converting the input string `s` into a set, which is an unordered collection of unique elements. If the set has more than one element, it means that there are duplicate characters in the string, and the function returns `False`. If the set has only one element, it means that all characters in the string are the same, and the function returns `True`. 

However, according to the given unit test, the function should return `False` when all characters in the string are not the same. Therefore, the function should return `True` when all characters in the string are the same. 

So, the correct function should be:

```python
def all_Characters_Same(s):
    return len(set(s)) != 1
``` 