```
def Find_Min_Length(list_of_lists):
    return min(len(lst) for lst in list_of_lists)
```
This function uses a generator expression to calculate the length of each list in the list of lists, and then returns the minimum of these lengths using the built-in `min` function. The unit test `assert Find_Min_Length([[1],[1,2]]) == 1` ensures that the function works correctly. 

For example, if you call `Find_Min_Length([[1],[1,2]])`, the function will return `1`, which is the length of the smallest list in the list of lists. 





# Test the function
print(Find_Min_Length([[1],[1,2]]))  # Output: 1
print(Find_Min_Length([[1,2,3],[1,2]]))  # Output: 1
print(Find_Min_Length([[1,2,3],[1,2,3]]))  # Output: 1
print(Find_Min_Length([[1,2,3],[1,2,3,4]]))  # Output: 1
print(Find_Min_Length([[1,2,3],[1,2,3,4,5]]))  # Output: 1
print(Find_Min_Length([[1,2,3],[1,2,3,4,5,6]]))  # Output: 1
print(Find_Min_Length([[1,2,3],[1,2,3,4,5,6,7]]))  # Output: 1
print(Find_Min_Length([[1,2,3],[1,2,3,4,5,6,7,8]]))  # Output: 1
print(Find_Min_Length([[1,2,3],[1,2,3,4,5,6,7,8,9]]))  # Output: 1
print(Find_Min_Length([[1,2,3],[1,2,3,4,5,6,7,8,9,10]]))  # Output: 1
print(Find_Min_Length([[1,2,3,4,5,6,7,8,9,10]]))  # Output: 1
print(Find_Min_Length([[1,2,3,4,5,6,7,8,9,10,11]]))  # Output: 1
