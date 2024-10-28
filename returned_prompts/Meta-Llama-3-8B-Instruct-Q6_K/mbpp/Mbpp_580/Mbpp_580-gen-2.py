```
def extract_even(nested_tuple):
    result = []
    for element in nested_tuple:
        if isinstance(element, tuple):
            result.append(extract_even(element))
        elif element % 2 == 0:
            result.append(element)
    return tuple(result)
```


Here is the explanation of the code:

1. The function `extract_even` takes a nested mixed tuple as an argument.
2. It initializes an empty list `result` to store the even elements.
3. It iterates over each element in the tuple. If the element is a tuple, it recursively calls `extract_even` on that tuple and appends the result to `result`.
4. If the element is not a tuple and it's even (i.e., `element % 2 == 0`), it appends the element to `result`.
5. Finally, it returns the `result` as a tuple.

The unit test `assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)` ensures that the function correctly extracts even elements from a nested mixed tuple. For example, it correctly removes the odd element `5` and returns the even elements `(4, 6, 2, 4, 6, 8)` in the correct order.