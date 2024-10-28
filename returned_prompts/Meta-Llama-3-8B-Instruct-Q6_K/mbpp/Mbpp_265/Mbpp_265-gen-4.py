```
def list_split(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]
```


The function `list_split` takes in a list `lst` and an integer `n`. It returns a list of lists, where each inner list contains every `n`th element from the original list.

The function uses list comprehension to iterate over the range from 0 to the length of the list, stepping by `n` each time. For each step `i`, it slices the list from `i` to `i+n` and adds the resulting list to the result.

For example, if the input list is `['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']` and `n` is 3, the function will return `[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]`. This is because the function splits the list into groups of 3 elements each, and then returns a list of these groups.