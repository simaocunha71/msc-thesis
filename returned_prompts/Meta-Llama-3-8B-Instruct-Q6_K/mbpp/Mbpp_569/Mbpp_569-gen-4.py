```
def sort_sublists(list_of_lists):
    return [sorted(sublist) for sublist in list_of_lists]
```





The problem is asking to sort each sublist of strings in a given list of lists. For example, if the input is [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']], the output should be [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']].

The unit test provided is:
assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]

To solve this problem, we can use a list comprehension to sort each sublist in the input list. The sorted function is used to sort each sublist. Here is the solution:
```
def sort_sublists(list_of_lists):
    return [sorted(sublist) for sublist in list_of_lists]
```
This function takes a list of lists as input, and returns a new list of lists where each sublist is sorted. The sorted function is used to sort each sublist, and the result is a new list of lists where each sublist is sorted.