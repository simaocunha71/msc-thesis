```
def even_position(lst):
    for i in range(0, len(lst), 2):
        if lst[i]%2 != 0:
            return False
    return True
```
The function `even_position(lst)` takes a list `lst` as an argument. It iterates over the list with a step of 2, which means it checks every even index. If it finds an even index that contains an odd number, it immediately returns `False`. If it checks all even indices and finds that they all contain even numbers, it returns `True`.

The unit test `assert even_position([3,2,1]) == False` shows that the function should return `False` when an even index contains an odd number. This is because the function is supposed to return `True` only when every even index contains an even number. If the list is `[3,2,1]`, the even index `0` contains the odd number `3`, so the function should return `False`. 





