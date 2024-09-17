```
def sort_sublists(list_of_lists):
    return [sorted(sublist) for sublist in list_of_lists]
```
The function `sort_sublists` takes a list of lists as an argument. It uses a list comprehension to iterate over each sublist in the list of lists. For each sublist, it uses the built-in `sorted` function to sort the sublist in ascending order. The sorted sublists are then returned as a new list of lists. 

The unit test `assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]` ensures that the function correctly sorts each sublist. The expected output is a list of lists where each sublist is sorted in ascending order. 