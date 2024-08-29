```python
def cummulative_sum(tuples):
    total = 0
    for t in tuples:
        total += sum(t)
    return total

print(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]))  # Should print: 30
```

