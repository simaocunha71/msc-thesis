```python
def count_pairs(list):
    count = 0
    for i in range(len(list)):
        for j in range(i, len(list)):
            if list[i] != list[j]:
                count += 1
    return count
```
