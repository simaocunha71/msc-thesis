```
def sort_sublists(lst):
    return [sorted(sublist) for sublist in lst]
```
The function `sort_sublists` takes a list of lists as input, where each sublist contains strings. It uses a list comprehension to iterate over each sublist, sorts the strings in the sublist using the built-in `sorted` function, and returns a new list with the sorted sublists.

For example, if the input is `[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]`, the function returns `[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]`, which are the sorted sublists. 

This function passes the given unit test:
```
assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
```  ```python
```
The function `sort_sublists` takes a list of lists as input, where each sublist contains strings. It uses a list comprehension to iterate over each sublist, sorts the strings in the sublist using the built-in `sorted` function, and returns a new list with the sorted sublists.

For example, if the input is `[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]`, the function returns `[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]`, which are the sorted sublists. 

This function passes the given unit test:
```
assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
```  ```python
```
The function `sort_sublists` takes a list of lists as input, where each sublist contains strings. It uses a list comprehension to iterate over each sublist, sorts the strings in the sublist using the built-in `sorted` function, and returns a new list with the sorted sublists.

For example, if the input is `[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]`, the function returns `[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]`, which are