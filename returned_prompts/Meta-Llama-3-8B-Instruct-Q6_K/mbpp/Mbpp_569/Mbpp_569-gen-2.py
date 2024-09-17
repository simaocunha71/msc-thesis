```
def sort_sublists(list_of_lists):
    return [sorted(sublist) for sublist in list_of_lists]
```


This function uses a list comprehension to iterate over each sublist in the list of lists. For each sublist, it uses the built-in `sorted` function to sort the strings in the sublist. The result is a new list of lists, where each sublist is sorted. 

The unit test `assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]` ensures that the function works correctly. It checks that the output of the function is a list of lists, where each sublist is sorted. 

This function assumes that the input is a list of lists, where each sublist contains only strings. If the input can contain other types of data, additional error checking may be needed. 

Note: The function does not modify the original list. It returns a new list with the sublists sorted. If you want to modify the original list, you can assign the result back to the original list. For example, `list_of_lists = sort_sublists(list_of_lists)`. 

This function has a time complexity of O(n*m*log(m)), where n is the number of sublists and m is the maximum length of a sublist. This is because the `sorted` function has a time complexity of O(n*log(n)) and we are calling it for each sublist. 

The space complexity is O(n*m), because we are creating a new list of lists, where each sublist is a copy of the corresponding sublist in the original list. The `sorted` function returns a new list, so we need to store the result somewhere. 

If you need to sort the sublists in-place (i.e., without using extra space), you can use the `sort` method instead of the `sorted` function. This would modify the original list, rather than creating a new list. However, this would also make the function less flexible and less easy to test. 

Here is an example of how you could use the `sort` method:

```
def sort_sublists_in_place(list_of_lists):
    for sublist in list_of_lists:
        sublist.sort()
    return list_of_lists
```

This function has the same time complexity as the original function, but the space complexity is O(1), because it does not use any extra space.