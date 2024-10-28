```
def unique_digits(x):
    return sorted([i for i in x if not any(int(d) % 2 == 0 for d in str(i))])
```
This function uses a list comprehension to iterate over the input list `x`. For each element `i` in `x`, it checks if any of the digits in the string representation of `i` is even (i.e., `int(d) % 2 == 0`). If no even digits are found, `i` is included in the resulting list. The `any` function returns `True` if at least one element of the iterable is true, and `False` otherwise.

The list comprehension is then converted to a list and sorted in increasing order using the `sorted` function. The resulting list is returned as the output of the function.