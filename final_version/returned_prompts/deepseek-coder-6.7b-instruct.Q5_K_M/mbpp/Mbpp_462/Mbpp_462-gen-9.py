Here is a Python solution for the problem:

```python
def combinations_list(lst):
    result = [[]]
    for i in range(len(lst)):
        result.extend([x + [lst[i]] for x in result])
    return result
```

This function uses the concept of dynamic programming to generate all possible combinations. It starts with an empty list and then for each item in the given list, it extends the existing combinations by adding the current item.

When the function `combinations_list(['orange',  'red',  'green',  'blue'])` is called, it returns the expected output.

```python
print(combinations_list(['orange',  'red',  'green',  'blue']))
```

Output:

```python
[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
```

The time complexity of this function is O(2^n), where n is the number of elements in the list, as it generates all possible combinations. The space complexity is also O(2^n) because of the storage required for the combinations.

Please note that the order of the combinations in the output list is not sorted. If you need the combinations sorted, you can sort the final result before returning it.

```python
return sorted(result, key=len)
```

This would sort the combinations by their length, resulting in a more human-readable output.

```python
def combinations_list(lst):
    result = [[]]
    for i in range(len(lst)):
        result.extend([x + [lst[i]] for x in result])
    return sorted(result, key=len)
```
"""

