Here is a Python function that solves the problem:

```python
def similar_elements(list1, list2):
    return list(set(list1) & set(list2))

print(similar_elements((3, 4, 5, 6), (5, 7, 4, 10)))
```

This function converts the input lists into sets and then uses the intersection (&) operator to find the common elements. Finally, it converts the result back into a list.