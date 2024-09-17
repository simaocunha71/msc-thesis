You can use the built-in functions `zip` and `map` to achieve this. The `zip` function pairs up the elements of the two tuples, and the `map` function applies the modulo operation to each pair.

Here is the Python code for the function:

```
def tuple_modulo(t1, t2):
    return tuple(map(lambda x, y: x % y, t1, t2))
```

This function works by iterating over the elements of the two tuples in parallel, using the `zip` function, and for each pair of elements, applying the modulo operation using a lambda function. The result is a new tuple containing the results of these operations.

For example, if you call `tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5))`, the function will return `(0, 4, 5, 1)`, which is the result of the element-wise modulo operation. The first element of the result is `10 % 5 = 0`, the second element is `4 % 6 = 4`, the third element is `5 % 7 = 5`, and the fourth element is `6 % 5 = 1`.