You can use the built-in functions `max` and `len` to find the element with the maximum length in a list. Here is the Python function:

```
def Find_Max(lst):
    return max(lst, key=len)
```

This function works by using the `max` function with the `key` argument set to `len`, which means it will compare the elements of the list based on their lengths. The `max` function then returns the element with the maximum length. 

For example, if you call `Find_Max([['A'],['A','B'],['A','B','C']])`, it will return `['A','B','C']`, which is the element with the maximum length in the list. 