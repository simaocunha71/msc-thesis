```
def even_position(lst):
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            return False
    return True
```
The function `even_position` takes a list of integers as input and checks whether every even index contains even numbers. It iterates over the list with a step size of 2, meaning it checks every even index. If it finds an index with an odd number, it immediately returns `False`. If it checks all even indices without finding an odd number, it returns `True`.

The unit test `assert even_position([3,2,1]) == False` ensures that the function correctly handles the case where an even index contains an odd number. In this case, the function should return `False`.