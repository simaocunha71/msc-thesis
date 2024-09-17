```
def flatten_list(lst):
    result = []
    for i in lst:
        if type(i) == list:
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result
```


The function takes a list as an argument and returns a new list with all the nested lists flattened.

Here's how it works:

1. It initializes an empty list `result` to store the flattened elements.
2. It iterates over each element `i` in the input list `lst`.
3. If `i` is a list itself, it recursively calls `flatten_list(i)` to flatten that list and extends the `result` list with the flattened elements.
4. If `i` is not a list, it simply appends `i` to the `result` list.
5. Finally, it returns the `result` list.

For example, given the input list `[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]`, the function will return the flattened list `[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]`.