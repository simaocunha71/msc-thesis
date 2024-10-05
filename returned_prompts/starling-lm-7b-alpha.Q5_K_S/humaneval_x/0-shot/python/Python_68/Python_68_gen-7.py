
def pluck(arr):
    smallest_index = 0
    smallest_even = None
    for i in range(len(arr)):
        if arr[i] % 2 == 0 and (smallest_even == None or arr[i] < smallest_even or (arr[i] == smallest_even and arr[i] < arr[smallest_index])):
            smallest_even = arr[i]
            smallest_index = i
    if smallest_even != None:
        return [smallest_even, smallest_index]
    else:
        return []


# Time:  O(n)
# Space: O(1)

```

```

```

```

```python

```

```

```python

```

```python

```

```python

```

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```
```python

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

