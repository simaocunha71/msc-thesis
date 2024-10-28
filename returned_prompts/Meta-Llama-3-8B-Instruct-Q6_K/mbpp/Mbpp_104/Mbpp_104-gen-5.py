```
def sort_sublists(lst):
    return [sorted(sublist) for sublist in lst]
``` 

This function uses a list comprehension to iterate over each sublist in the input list. For each sublist, it sorts the elements using the built-in `sorted` function and returns a new list with the sorted sublists. The result is a new list of lists, where each sublist is sorted. 

The unit test `assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]` ensures that the function works correctly for the given input. 
```python
assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
```  ```python
assert sort_sublists([])==[]
``` 
```python
assert sort_sublists([['a', 'b'], ['c', 'd', 'e'], ['f', 'g', 'h', 'i']]) == [['a', 'b'], ['c', 'd', 'e'], ['f', 'g', 'h', 'i']]
```  ```python
assert sort_sublists([['a', 'b'], ['b', 'a'], ['c', 'c', 'c']]) == [['a', 'b'], ['a', 'b'], ['c', 'c', 'c']]
```  ```python
assert sort_sublists([['a', 'b'], ['c', 'd'], []]) == [['a', 'b'], ['c', 'd'], []]
```  ```python
assert sort_sublists([[1, 2], [3, 4], [5, 6]]) == [[1, 2], [3, 4], [5, 6]]
```  ```python
assert sort_sublists([['a', 'b'], ['c', 'd', 'e'], [1, 2, 3]]) == [['a', 'b'], ['c', 'd', 'e'], [1, 2, 3]]
```  ```python
assert sort_sublists([['a', 'b'], ['c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j