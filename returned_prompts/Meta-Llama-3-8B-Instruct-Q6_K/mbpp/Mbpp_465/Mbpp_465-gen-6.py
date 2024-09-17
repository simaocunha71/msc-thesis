The task is to create a function that takes a dictionary as an input and returns a new dictionary with all empty items (i.e., items with values that are None or empty strings) removed.

Based on the provided unit test, we can assume that "empty" items are those with values that are None or empty strings. The unit test `assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}` suggests that the function should remove the item with key 'c3' because its value is None.

Here is the Python function to solve this problem:
```
def drop_empty(d):
    return {key: value for key, value in d.items() if value is not None and value != ''}
```
This function uses a dictionary comprehension to create a new dictionary that includes only the items from the original dictionary where the value is not None and not an empty string. The `if value is not None and value != ''` condition in the comprehension ensures that only non-empty items are included in the new dictionary. 