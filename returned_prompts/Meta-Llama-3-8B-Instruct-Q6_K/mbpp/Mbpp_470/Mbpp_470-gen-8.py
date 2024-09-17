```
def add_pairwise(t):
    return tuple(x + y for x, y in zip(t, t[1:]))
```
This function uses the built-in `zip` function to iterate over the tuple and its slice (excluding the first element). It then uses a generator expression to add each pair of neighboring elements together. The result is a new tuple containing the pairwise additions. The unit test `assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)` demonstrates that the function works as expected.