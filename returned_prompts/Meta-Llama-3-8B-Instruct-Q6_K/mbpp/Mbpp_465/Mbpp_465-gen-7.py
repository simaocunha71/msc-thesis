```
def drop_empty(d):
    return {k: v for k, v in d.items() if v}
```


This function uses a dictionary comprehension to create a new dictionary that includes only the key-value pairs from the original dictionary where the value is not None. The `if v` condition in the comprehension filters out the key-value pairs where the value is None.

The unit test `assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}` ensures that the function correctly drops the key-value pair where the value is None.