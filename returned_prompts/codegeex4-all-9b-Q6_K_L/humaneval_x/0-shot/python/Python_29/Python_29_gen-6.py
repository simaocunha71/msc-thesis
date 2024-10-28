```python
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

print(filter_by_prefix([], 'a'))
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))
```
