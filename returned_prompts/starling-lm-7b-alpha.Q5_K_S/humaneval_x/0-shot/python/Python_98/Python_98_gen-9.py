
```python
def count_upper(s):
    count = 0
    for i, char in enumerate(s):
        if char.upper() in 'AEIOU' and i % 2 == 0:
            count += 1
    return count
```

To test the function,