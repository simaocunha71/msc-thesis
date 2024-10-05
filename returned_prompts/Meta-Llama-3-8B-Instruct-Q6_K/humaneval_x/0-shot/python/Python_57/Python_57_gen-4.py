```
def monotonic(l: list):
    return (all(l[i] <= l[i+1] for i in range(len(l)-1)) or
            all(l[i] >= l[i+1] for i in range(len(l)-1)))
```



This function checks if the list elements are monotonically increasing or decreasing. It uses two conditions:

1. All elements are in increasing order (`all(l[i] <= l[i+1] for i in range(len(l)-1))`)
2. All elements are in decreasing order (`all(l[i] >= l[i+1] for i in range(len(l)-1))`)

It returns `True` if either condition is met, and `False` otherwise. The `all` function is used to check if all elements in the list satisfy the given condition. The `or` operator is used to combine the two conditions.

The unit tests provided show that the function works correctly:

* `monotonic([1, 2, 4, 20])` returns `True` because the list is monotonically increasing.
* `monotonic([1, 20, 4, 10])` returns `False` because the list is not monotonically increasing or decreasing.
* `monotonic([4, 1, 0, -10])` returns `True` because the list is monotonically decreasing.