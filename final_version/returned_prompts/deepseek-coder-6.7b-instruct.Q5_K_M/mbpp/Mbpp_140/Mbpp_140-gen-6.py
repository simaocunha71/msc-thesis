```python
def extract_singly(lst):
    flattened = []
    for sublist in lst:
        for item in sublist:
            flattened.append(item)
    return flattened

print(set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])))  # {1, 3, 4, 5, 7}
```

