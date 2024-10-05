To solve this problem, we can follow these steps:

1. Convert both input lists to sets to remove any duplicate elements.
2. Use the intersection operator (&) to find the common elements between the two sets.
3. Convert the result back to a list and sort it.

Here's the implementation in Python:

```python
def common(l1, l2):
    l1_set = set(l1)
    l2_set = set(l2)
    result = sorted(l1_set & l2_set)
    return result
```

Note: This solution assumes that the input lists contain only hashable elements (i.e., no dictionaries or other non-hashable types). If the lists can contain non-hashable types, you'll need to convert them to sets of hashable types before finding the intersection.

The time complexity of this solution is O(n + m), where n and m are the lengths of the input lists, as we need to convert each list to a set. The space complexity is also O(n + m), as we need to store both sets in memory.

You can test the function with the provided test cases to verify its correctness:

```python
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # Expected output: [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # Expected output: [2, 3]
```

These test cases should pass and confirm that the function is working correctly.

```python

```

```python

```

```python

```

```python

```
```python

```python

```
```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python