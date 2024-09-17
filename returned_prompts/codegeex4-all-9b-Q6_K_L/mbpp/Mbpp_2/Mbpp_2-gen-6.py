Here's a Python solution that uses the built-in `set` data type to find the shared elements between two lists:

```python
def similar_elements(list1, list2):
    return set(list1) & set(list2)

assert similar_elements([3, 4, 5, 6], [5, 7, 4, 10]) == set([4, 5])
```

This solution works by converting both lists to sets and then performing an intersection operation (`&`), which returns a set of shared elements. The `assert` statement at the end checks that the function works correctly.