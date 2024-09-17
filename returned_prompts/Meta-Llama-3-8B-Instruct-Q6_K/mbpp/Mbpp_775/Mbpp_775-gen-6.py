```
def odd_position(lst):
    return all(lst[i]%2==1 for i in range(1, len(lst), 2))
```
The function `odd_position` checks whether every odd index contains odd numbers of a given list. The function uses the built-in `all` function in combination with a generator expression. The generator expression `lst[i]%2==1 for i in range(1, len(lst), 2)` iterates over the elements at odd indices of the list and checks whether the remainder of the division of each element by 2 is 1. This means it checks whether the element is odd. The `all` function then checks whether this condition is true for all elements, i.e., whether every odd index contains an odd number. 

The unit test `assert odd_position([2,1,4,3,6,7,6,3]) == True` ensures that the function works correctly. 

This function assumes that the input list is not empty. If the list can be empty, you should add a check at the beginning of the function to return `True` for an empty list. 
```python
def odd_position(lst):
    if not lst:
        return True
    return all(lst[i]%2==1 for i in range(1, len(lst), 2))
``` 