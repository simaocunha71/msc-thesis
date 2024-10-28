Here is the Python code that solves the problem:

```python
def common(l1, l2):
    set1 = set(l1)
    set2 = set(l2)
    return sorted(list(set1 & set2))
```
Explanation:
1. We convert the input lists to sets in order to find the common elements efficiently.
2. We use the set intersection operator (&) to find the common elements.
3. We convert the result back to a list and sort it before returning.

This function works as expected:

```python
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
# Output: [1, 5, 653]

print(common([5, 3, 2, 8], [3, 2]))
# Output: [2, 3]
```



