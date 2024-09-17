```
def Find_Max(lst):
    return max(lst, key=len)
```


The function `Find_Max` takes a list of lists as input and returns the list with the maximum length. It uses the built-in `max` function with the `key` argument set to `len` to find the list with the maximum length. The `max` function returns the first list it encounters with the maximum length, which is why the function returns the first list it finds with the maximum length in case of a tie. If you want to return all lists with the maximum length, you would need to use a different approach, such as using a list comprehension to filter the lists based on their length, and then returning the filtered list. Here is an example of how you could do that:

```
def Find_Max(lst):
    max_len = max(len(i) for i in lst)
    return [i for i in lst if len(i) == max_len]
```

This function first finds the maximum length of the lists in the input list using a generator expression. It then uses a list comprehension to create a new list that includes only the lists with the maximum length. This list is then returned. This function will return all lists with the maximum length, not just the first one it finds. If you want to return only the first list with the maximum length, you can use the original function. If you want to return all lists with the maximum length and there are multiple lists with the same maximum length, you can use this modified function.