```
def sort_sublists(lst):
    return [sorted(sublist) for sublist in lst]
```
The function `sort_sublists` takes a list of lists as an argument, where each sublist contains strings. It uses a list comprehension to iterate over each sublist in the input list, sorts the sublist in ascending order using the `sorted` function, and returns a new list with the sorted sublists. The original list remains unchanged.

The unit test `assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]` ensures that the function works correctly. It checks that the output of the function is a list of lists, where each sublist is a sorted version of the corresponding sublist in the input list.