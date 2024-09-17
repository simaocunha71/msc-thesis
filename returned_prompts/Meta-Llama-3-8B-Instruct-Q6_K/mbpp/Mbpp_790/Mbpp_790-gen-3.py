```
def even_position(lst):
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            return False
    return True
```


The given function `even_position` checks whether every even index in a given list contains even numbers. It iterates over the list with a step of 2 (i.e., it checks every even index) and returns `False` as soon as it finds an odd number at an even index. If it doesn't find any odd numbers at even indices, it returns `True`. This function uses the unit test `assert even_position([3,2,1]) == False` to verify its correctness.