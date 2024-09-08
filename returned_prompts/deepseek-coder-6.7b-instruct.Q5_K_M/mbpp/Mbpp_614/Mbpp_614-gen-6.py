```python
def cummulative_sum(lst):
    total_sum = 0
    for tup in lst:
        total_sum += sum(tup)
    return total_sum

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]))  # Output: 30
```

This function works by iterating over each tuple in the input list. For each tuple, it adds the sum of the values to a running total, which it returns at the end.

Note: This function assumes that all elements in the tuple are numeric and does not handle non-numeric types. If you need to handle such cases, you would need to modify the function accordingly.

