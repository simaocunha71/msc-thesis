Here is the Python program that solves the problem:

```python
def combinations_list(lst):
    result = [[]]
    for i in range(len(lst)):
        result.extend([x + [lst[i]] for x in result])
    return result

print(combinations_list(['orange', 'red', 'green', 'blue']))
```

This function generates all possible combinations of the elements of a given list using the concept of list comprehension in Python. The list comprehension `[x + [lst[i]] for x in result]` generates all combinations by appending each element of the original list to each list in `result`. The `extend` method then adds these new combinations to `result`.

The program returns all possible combinations of the elements of the list `['orange', 'red', 'green', 'blue']`.
"""
assert combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
"""
"""
assert combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
"""
"""
assert combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue',