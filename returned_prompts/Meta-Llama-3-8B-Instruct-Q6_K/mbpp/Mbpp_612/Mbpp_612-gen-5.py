```
def merge(list_of_lists):
    first_lists = [sublist[0] for sublist in list_of_lists]
    second_lists = [sublist[1] for sublist in list_of_lists]
    return [first_lists, second_lists]
```


This function uses list comprehension to create two lists, one for the first elements of each sublist and one for the second elements. It then returns these two lists as a list of lists. The unit test provided ensures that the function works correctly. 

For example, if we call `merge([['x', 'y'], ['a', 'b'], ['m', 'n']])`, the function will return `[['x', 'a', 'm'], ['y', 'b', 'n']]`.  This is because the first list contains the first element of each sublist, and the second list contains the second element of each sublist.  The order of the elements in the lists is the same as the order of the sublists in the input list. 

This function assumes that all sublists have exactly two elements.  If a sublist has a different number of elements, the function may not work correctly.  If you need to handle sublists with different numbers of elements, you may need to add error checking code to handle this case.  For example, you could check that each sublist has exactly two elements, and raise an exception if a sublist has a different number of elements.  Here is an example of how you could do this:

```
def merge(list_of_lists):
    for sublist in list_of_lists:
        if len(sublist) != 2:
            raise ValueError("All sublists must have exactly two elements")
    first_lists = [sublist[0] for sublist in list_of_lists]
    second_lists = [sublist[1] for sublist in list_of_lists]
    return [first_lists, second_lists]
```

This version of the function will raise a ValueError if it encounters a sublist that has a different number of elements.  You could also add code to handle this case in some other way, such as by ignoring the sublist or by replacing it with a default value.  It depends on what you need to do in this case.  For example, you could replace the sublist with a default value like this:

```
def merge(list_of_lists):
    for i, sublist in enumerate(list_of_lists):
        if len(sublist) != 2:
            list_of_lists[i] = ['default', 'default']
