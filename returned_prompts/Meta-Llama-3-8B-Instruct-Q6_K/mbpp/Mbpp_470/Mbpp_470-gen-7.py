```
def add_pairwise(t):
    return tuple(a + b for a, b in zip(t, t[1:]))
```



The function takes a tuple as input and returns a new tuple containing the pairwise sum of the neighboring elements. The `zip` function is used to pair up the elements from the tuple with the elements from the tuple shifted by one position. The `tuple` function is used to convert the result into a tuple. The unit test `assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)` ensures that the function works correctly.