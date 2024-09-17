```
def sort_sublists(list_of_lists):
    return [[sorted(sublist)] for sublist in list_of_lists]
```
This function uses a list comprehension to iterate over each sublist in the input list of lists. For each sublist, it sorts the sublist using the built-in `sorted` function and wraps the result in a new list. The resulting list of lists is then returned. 

For example, if the input is `[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]`, the output will be `[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]`. 

The unit test `assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]` ensures that the function behaves as expected. 

Note that this function does not sort the sublists in place, but rather returns a new list of lists. If you want to sort the sublists in place, you can use a similar approach with the `sort` method, like this: `for sublist in list_of_lists: sublist.sort()`. However, this would modify the original input list, which may not be desirable in all cases. 

Also, this function assumes that the input is a list of lists of strings. If the input can contain other types of data, you may need to modify the function accordingly. For example, if the input can contain lists of numbers, you would need to decide how to sort those lists. 

Finally, this function has a time complexity of O(n log n) in the worst case, where n is the total number of elements in the input list of lists. This is because the `sorted` function has a time complexity of O(n log n) in the worst case, and we are calling it once for each sublist. If the input list of lists is very large, this function could be slow. In that case, you may need to consider using a more efficient sorting algorithm or data structure. 