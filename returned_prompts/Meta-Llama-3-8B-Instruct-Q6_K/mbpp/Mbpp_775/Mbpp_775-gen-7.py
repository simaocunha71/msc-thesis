```
def odd_position(lst):
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            return False
    return True
```
The function `odd_position` checks whether every odd index in the given list `lst` contains an odd number. It iterates over the list with a step of 2, starting from the first element (index 1). If it finds an even number at an odd index, it immediately returns `False`. If it checks all elements without finding an even number at an odd index, it returns `True`. The unit test `assert odd_position([2,1,4,3,6,7,6,3]) == True` ensures that the function works correctly. 