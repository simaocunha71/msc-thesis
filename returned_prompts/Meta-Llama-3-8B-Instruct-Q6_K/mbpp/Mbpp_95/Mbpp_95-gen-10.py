```
def Find_Min_Length(lists):
    min_length = min(len(lst) for lst in lists)
    return min_length
```
This function uses a generator expression to iterate over the lists in the input list and calculate the length of each list. The built-in `min` function is then used to find the smallest length. The function returns the smallest length. 

The unit test `assert Find_Min_Length([[1],[1,2]]) == 1` shows that the function should return the smallest length in the input list of lists. In this case, the smallest length is 1. 

This function will work with any list of lists, not just those containing single-digit integers. It will return the smallest length in the list, regardless of the contents of the lists.  For example, `Find_Min_Length([[1,2,3],[4,5,6],[7,8,9]])` would return 3, because the smallest length in the input list is 3.  Similarly, `Find_Min_Length([[1,2,3],[4,5,6,7],[8,9,10,11,12]])` would return 3, because the smallest length in the input list is 3.  



It's worth noting that this function will return the smallest length, even if there are multiple lists with the same smallest length. For example, `Find_Min_Length([[1,2],[1,2,3],[1,2]])` would return 2, because two of the lists have length 2, which is the smallest length in the input list. If you want the function to return the first list it encounters with the smallest length, you would need a slightly different implementation.  For example, you could use the `min` function with a key function that returns a tuple containing the length of each list and the list itself.  This would allow the function to return the first list it encounters with the smallest length, in case of a tie.  Here is an example of how you could implement this:

```
def Find_Min_Length(lists):
    return min((len(lst), lst) for lst in lists)[1]
```

This function uses a generator expression to create a list of tuples, where each tuple contains the length of a list and the list itself. The `min` function is then used to find the tuple with the smallest length. The function returns the list itself, rather than the length.  This will return the first list it