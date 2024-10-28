```
def sort_sublists(lst):
    return [sorted(sublist) for sublist in lst]
```




```
def sort_sublists(lst):
    return [sorted(sublist) for sublist in lst]
```



The function `sort_sublists` takes a list of lists as input, where each sublist contains strings. It returns a new list of lists, where each sublist is sorted in ascending order.

The function uses a list comprehension to iterate over each sublist in the input list. For each sublist, it uses the built-in `sorted` function to sort the sublist and returns a new list containing the sorted sublists.

For example, if the input is `[["green", "orange"], ["black", "white"], ["white", "black", "orange"]]`, the function returns `[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]`.

The unit test `assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]` ensures that the function works correctly.