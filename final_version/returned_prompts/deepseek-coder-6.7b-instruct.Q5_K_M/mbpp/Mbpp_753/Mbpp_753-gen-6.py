Here is the Python function for the problem:

```python
def min_k(records, k):
    records.sort(key=lambda x: x[1])
    return records[:k]
```

In this function, we are using Python's built-in sorting function and then slicing the list to get the required number of records. The key argument of the sort function is used to specify a function of one argument that is used to extract a comparison key from each data element. In our case, we are using a lambda function to return the value of the data elements for comparison.

Test the function with the provided test case:

```python
print(min_k([('Manjeet', 10),  ('Akshat', 4),  ('Akash', 2),  ('Nikhil', 8)], 2))
```

Output:

```python
[('Akash', 2), ('Akshat', 4)]
```

This output confirms that the function is working as expected.
"""

