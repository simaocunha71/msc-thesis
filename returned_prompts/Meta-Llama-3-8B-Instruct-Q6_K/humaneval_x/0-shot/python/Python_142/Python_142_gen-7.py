Here is a Python function that does what you described:
```
def sum_squares(lst):
    return sum((x**2 if i % 3 == 0 else x**3 if i % 4 == 0 and i % 3 != 0 else x for i, x in enumerate(lst)))
```
Here's a breakdown of how the function works:

1. The `enumerate` function is used to iterate over the list with both the index `i` and the value `x`.
2. The ternary operator is used to determine what operation to apply to each value based on its index. If the index is a multiple of 3, square the value. If the index is a multiple of 4 but not 3, cube the value. Otherwise, leave the value unchanged.
3. The `sum` function is used to add up all the transformed values.

Here are some examples to demonstrate the function's behavior:
```
>>> sum_squares([1, 2, 3])
6
>>> sum_squares([])
0
>>> sum_squares([-1, -5, 2, -1, -5])
-126
```  