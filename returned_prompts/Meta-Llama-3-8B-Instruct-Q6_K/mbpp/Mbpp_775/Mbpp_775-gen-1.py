```
def odd_position(lst):
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            return False
    return True
```


The function `odd_position(lst)` takes a list `lst` as an argument and checks whether every odd index contains an odd number. It uses a for loop to iterate over the list, starting from the first odd index (1) and stepping by 2 each time. For each index, it checks if the value at that index is even (i.e., `lst[i] % 2 == 0`). If it finds an even number, it immediately returns `False`. If it goes through the entire loop without finding an even number, it returns `True`.

The unit test `assert odd_position([2,1,4,3,6,7,6,3]) == True` ensures that the function behaves correctly. In this test, the list contains both even and odd numbers, but every odd index contains an odd number. The function should return `True`, which it does.