```
def check_K(tup, k):
    return k in tup
```
The function `check_K` takes two parameters, `tup` (a tuple) and `k` (an integer). It returns `True` if `k` is present in `tup`, and `False` otherwise.

The unit test `assert check_K((10, 4, 5, 6, 8), 6) == True` suggests that the function should return `True` when `k` is present in the tuple, and `False` otherwise.

The solution uses the `in` operator to check if `k` is present in `tup`. This operator returns `True` if `k` is found in `tup`, and `False` otherwise. Therefore, the function simply returns the result of `k in tup`.