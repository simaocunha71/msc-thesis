```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]
```
```python
filter_integers(['a', 3.14, 5])
# Output: [5]
filter_integers([1, 2, 3, 'abc', {}, []])
# Output: [1, 2, 3]
```
