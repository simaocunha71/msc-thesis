The problem asks to sort a dictionary by its values. However, dictionaries in Python are inherently unordered, so this is not possible. 

The unit test provided suggests that the desired output is a list of tuples, where each tuple contains a key-value pair from the dictionary, sorted by the values. 

Here is a Python function that accomplishes this:

```python
def sort_counter(counter):
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)
```

This function uses the built-in `sorted` function to sort the dictionary items (which are stored in a list of tuples) by their values. The `key` argument of the `sorted` function is a function that takes a tuple (a key-value pair from the dictionary) and returns the value from that tuple. The `reverse=True` argument is used to sort the items in descending order (i.e., the dictionary values that are largest will come first in the output list). 

The function returns the sorted list of tuples. 

For example, if we call `sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})`, the function will return `[('Chemistry', 87), ('Physics', 83), ('Math', 81)]`, which is the desired output. 





This solution assumes that the dictionary is not empty and that all values are hashable (i.e., they can be used as keys in a dictionary). If these assumptions are not valid, additional error checking may be necessary.