```
def odd_position(lst):
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            return False
    return True
```
The function `odd_position` takes a list `lst` as input and returns `True` if every odd index contains an odd number, and `False` otherwise. It iterates over the list, starting from the first odd index (1), and checks if the number at each index is odd. If it finds an even number at an odd index, it immediately returns `False`. If it checks all indices and doesn't find any even numbers, it returns `True`. The unit test `assert odd_position([2,1,4,3,6,7,6,3]) == True` ensures that the function works correctly.  """

