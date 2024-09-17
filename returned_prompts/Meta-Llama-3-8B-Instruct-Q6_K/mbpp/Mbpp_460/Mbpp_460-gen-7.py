```
def Extract(lst):
    return [sublist[0] for sublist in lst]
``` 
The function Extract takes a list of lists (lst) as input. It uses list comprehension to iterate over each sublist in the list, and for each sublist, it extracts the first element and adds it to the output list. The function returns the list of first elements from each sublist. This function passes the given unit test:
```
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
``` 
This function works by iterating over each sublist in the input list, and for each sublist, it takes the first element and adds it to the output list. The output list is then returned. The unit test provided ensures that the function works correctly for the given input. 





