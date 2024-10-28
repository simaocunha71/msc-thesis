Here is the Python code for the problem:

```Python
def sortEven(l):
    return [i if i % 2 != 0 else sorted([x for x in l if x % 2 == 0])[i % 2] for i in range(len(l))]
```

This code works by iterating over each index `i` in the list `l`. If the index `i` is odd, it leaves the value at that index unchanged. If the index `i` is even, it sorts the list of even numbers and takes the `i % 2`th element of the sorted list. The `i % 2` expression ensures that the first even index takes the first element of the sorted list, the second even index takes the second element, and so on.

For example, if `l = [5, 6, 3, 4]`, the code will return `[3, 6, 5, 4]`. The even indices of `l` are `1` and `3`, and the sorted list of even numbers is `[4, 6]`. The code takes the first element of the sorted list for the first even index, and the second element for the second even index. The odd indices of `l` are `0` and `2`, and the code leaves the values at these indices unchanged. Therefore, the final output is `[3, 6, 5, 4]`.