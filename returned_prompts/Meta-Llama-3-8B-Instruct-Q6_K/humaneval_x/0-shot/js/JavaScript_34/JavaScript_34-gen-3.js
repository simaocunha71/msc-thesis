```python
def unique(l):
    return sorted(set(l))
```
The function `unique` takes a list `l` as input, converts it to a set (which removes duplicates), and then converts it back to a list and sorts it. The result is a list of unique elements in sorted order. For example:
```python
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [0, 2, 3, 5, 9, 123]
``` Q.E.D. 🎉

