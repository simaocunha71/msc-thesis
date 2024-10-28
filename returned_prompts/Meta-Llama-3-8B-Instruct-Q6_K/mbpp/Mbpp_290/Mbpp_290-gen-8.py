You can use the built-in max function with a custom key function that returns the length of each list. The max function will return the list with the maximum length.

Here's how you can do it:

```
def max_length(list_of_lists):
    return max(list_of_lists, key=len)
```

This function takes a list of lists as an argument, and returns the list with the maximum length. If there are multiple lists of the same maximum length, it will return the first one it encounters. If you want to return all lists of the maximum length, you would need to use a different approach.

Here's how you can modify the function to return all lists of the maximum length:

```
def max_length(list_of_lists):
    max_len = max(len(sublist) for sublist in list_of_lists)
    return max((sublist for sublist in list_of_lists if len(sublist) == max_len), key=len)
```

This function first finds the maximum length of all lists. Then it returns the first list it encounters that has this maximum length. If there are multiple lists of the same maximum length, it will return the first one it encounters. If you want to return all lists of the maximum length, you would need to modify the function further. For example, you could return a list of all lists of the maximum length:

```
def max_length(list_of_lists):
    max_len = max(len(sublist) for sublist in list_of_lists)
    return [sublist for sublist in list_of_lists if len(sublist) == max_len]
``` 