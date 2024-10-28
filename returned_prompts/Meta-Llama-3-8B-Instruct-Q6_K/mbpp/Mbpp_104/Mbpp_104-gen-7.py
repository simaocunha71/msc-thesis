```
def sort_sublists(list_of_lists):
    return [sorted(sublist) for sublist in list_of_lists]
```





This function uses a list comprehension to iterate over each sublist in the input list of lists. For each sublist, it uses the built-in `sorted` function to sort the sublist in-place and returns the sorted sublist. The result is a new list of lists, where each sublist is sorted.