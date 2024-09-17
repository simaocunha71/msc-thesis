```
def check_Consecutive(lst):
    return all(lst[i] + 1 == lst[i+1] for i in range(len(lst)-1))
```
The above function checks whether the given list contains consecutive numbers or not. It uses the `all()` function with a generator expression to check if the difference between each pair of consecutive elements is 1. If the list contains consecutive numbers, the function will return `True`; otherwise, it will return `False`. 

The unit test `assert check_Consecutive([1,2,3,4,5]) == True` ensures that the function works correctly for a list of consecutive numbers. 





The function will return `True` for the following inputs:
- `[1,2,3,4,5]`
- `[10,11,12,13,14]`
- `[20,21,22,23,24]`

And it will return `False` for the following inputs:
- `[1,2,4,5,6]`
- `[1,2,3,5,6]`
- `[1,3,5,7,9]`





The function will work correctly for lists of any length, not just those with 5 elements. For example, it will return `True` for the list `[1,2,3,4,5,6,7,8,9,10]` and `False` for the list `[1,2,4,5,6,7]`.