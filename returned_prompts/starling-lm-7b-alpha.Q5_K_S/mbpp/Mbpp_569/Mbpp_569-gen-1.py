```
def sort_sublists(lst):
    """
    >>> sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])
    [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
    """
    for i in range(len(lst)):
        lst[i].sort()
    return lst
```
    
    

This function will sort each sublist alphabetically. It uses a loop to go through each sublist, and the built-in `sort()` method to sort the strings in each sublist.

The `sort_sublists` function takes a list of lists as input and sorts the sublists in-place. It uses a loop to iterate through each sublist and the `sort()` method to sort the strings within each sublist. The function then returns the modified list of lists.

To use this function, you can call it with a list of lists as an argument. For example, if you want to sort the sublists of the list `[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]`, you can do so by calling `sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])`. The function will return `[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]`, which is the sorted list of lists.

To test the function, you can use the `assert` statement to check if the function returns the expected result. In this case, the expected result is `[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]`, so you can assert that the function returns this value by using `assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]`.

Overall, this function allows you to sort the sublists of a given list of lists in alphabetical order.

    
    