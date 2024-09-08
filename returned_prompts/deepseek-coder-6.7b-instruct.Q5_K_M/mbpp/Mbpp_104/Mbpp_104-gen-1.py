Here is the Python code to solve the problem:

```python
def sort_sublists(lst):
    result = []
    for sublist in lst:
        result.append(sorted(sublist))
    return result

print(sort_sublists([["green", "orange"], ["black", "white"], ["white", "black", "orange"]]))
```

This code defines a function `sort_sublists()` that takes a list of lists of strings as its argument. It creates an empty list `result` to store the sorted sublists. Then it iterates over each sublist in the input list, sorts it using the `sorted()` function, and appends the sorted sublist to the `result` list. Finally, it returns the `result` list.

The last line of the code calls the function with the given input and prints the result.

When you run this code, it will output:

```
[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
```

which is the expected sorted list of lists.
"""

