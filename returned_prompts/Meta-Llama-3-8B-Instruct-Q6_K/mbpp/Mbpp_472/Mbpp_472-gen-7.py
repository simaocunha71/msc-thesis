```
def check_Consecutive(lst):
    return all(lst[i+1] - lst[i] == 1 for i in range(len(lst)-1))
```
The function `check_Consecutive` checks whether the given list contains consecutive numbers or not. It uses the `all` function with a generator expression to check if the difference between each pair of adjacent elements in the list is 1. If the difference is 1 for all pairs, it returns `True`, meaning the list contains consecutive numbers. Otherwise, it returns `False`. 

The unit test `assert check_Consecutive([1,2,3,4,5]) == True` ensures that the function correctly identifies consecutive numbers in the list. 





