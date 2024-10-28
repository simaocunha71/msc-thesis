```
def sort_sublists(list_of_lists):
    return [sorted(sublist) for sublist in list_of_lists]
```
The function `sort_sublists` takes a list of lists as an argument and returns a new list of lists where each sublist is sorted. It uses a list comprehension to iterate over the input list, and for each sublist, it uses the built-in `sorted` function to sort the sublist. The sorted sublists are then returned as a new list. The function is tested with the provided unit test, which checks that the function correctly sorts the sublists of the input list. 
```
assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
```  This test ensures that the function correctly sorts the sublists in the input list. If the function is correct, the output of the test will be `True`.  If the function is incorrect, the test will fail and report an error. 
```
print(sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"])))
``` This will print the output of the function for the provided test case. The output should be `[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]`.  If the output is different, the function is incorrect. 
```python
print(sort_sublists([["orange", "green"], ["white", "black"], ["black", "white", "orange"]]))
``` This will print the output of the function for another test case. The output should be `[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]`. If the output is different, the function is incorrect. 
```
print(sort_sublists([["green"], ["black"], ["orange", "white", "black"]]))
``` This will print the output of the function for another test case. The output should be `[['green'], ['black'], ['black', 'orange', 'white']]`. If the output is different, the function is incorrect. 
```python
print(sort_sublists([]))
``` This will print the output of the function for an empty list. The output should be `[]`. If the output is different, the function is incorrect. 
```python
print(sort_sublists([[]