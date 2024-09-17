```
def even_position(lst):
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            return False
    return True
```


The function `even_position` iterates over the list `lst` with a step of 2, which means it checks every even index. For each index, it checks if the value at that index is even by using the modulo operator `% 2`. If it finds a value that is not even (i.e., the remainder when divided by 2 is not 0), it immediately returns `False`. If it checks all even indices and doesn't find any odd values, it returns `True`. This function will return `False` for the input `[3,2,1]` as expected.