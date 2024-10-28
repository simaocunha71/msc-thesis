
```python
def get_total_number_of_sequences(m, n):
    count = 0
    for i in range(1, n+1):
        count += m-i+1
    return count
```


