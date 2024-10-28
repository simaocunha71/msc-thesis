```
def sort_sublists(lst):
    return [sorted(sublist) for sublist in lst]
```
The function `sort_sublists` takes a list of lists as input, where each sublist contains strings. It returns a new list of lists, where each sublist is sorted in ascending order. The `sorted` function is used to sort each sublist. The `sorted` function returns a new list containing all items from the input list in ascending order. This function works with Python 3.x.

Example:
```
assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
```  # test case
```
sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))
```  # example usage
```python
[sorted(sublist) for sublist in lst]
```
This line of code uses a list comprehension to create a new list of lists, where each sublist is the sorted version of the corresponding sublist in the input list. The `sorted` function is called on each sublist to sort it. The result is a new list of lists, where each sublist is sorted in ascending order. This is the desired output for the problem.  # example usage
```
print(sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"])))
```
This will output:
```
[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
```
which is the expected output for the given test case.  # output
```
```python
def sort_sublists(lst):
    return [sorted(sublist) for sublist in lst]
```
This function is a solution to the problem, which is to sort each sublist of strings in a given list of lists. The `sorted` function is used to sort each sublist, and the result is a new list of lists, where each sublist is sorted in ascending order. This function works with Python 3.x.  # solution
```
```python
assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
```  # test case
