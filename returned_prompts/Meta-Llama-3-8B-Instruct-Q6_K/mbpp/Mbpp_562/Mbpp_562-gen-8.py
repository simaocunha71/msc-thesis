```
def Find_Max_Length(lst):
    return max(len(sublist) for sublist in lst)
```
The problem is asking to write a function that finds the length of the longest sublist in a given list of lists. The function should take a list of lists as input and return the length of the longest sublist.

The unit test provided is `assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4`. This test case indicates that the longest sublist has a length of 4.

Here is a Python solution for the problem:
```
def Find_Max_Length(lst):
    return max(len(sublist) for sublist in lst)
```
This function uses a generator expression to calculate the length of each sublist and then returns the maximum length using the built-in `max` function. The `len` function is used to get the length of each sublist, and the `max` function is used to find the maximum length among all sublists. The function can handle a list of lists of any length and returns the length of the longest sublist.