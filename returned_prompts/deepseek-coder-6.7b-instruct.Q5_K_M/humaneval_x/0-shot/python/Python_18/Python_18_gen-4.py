
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    while substring in string:
        count += 1
        string = string[string.find(substring)+1:]
    return count
```

## Task 4:

