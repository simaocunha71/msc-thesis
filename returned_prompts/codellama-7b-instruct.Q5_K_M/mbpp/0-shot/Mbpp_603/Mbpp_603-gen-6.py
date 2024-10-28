```python
def get_ludic(n):
    ludic = [1]
    while ludic[-1] < n:
        ludic.append(ludic[-1] + ludic[-2])
    return ludic[:n]
```