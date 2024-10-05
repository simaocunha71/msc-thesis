
def pluck(arr):
    even_val = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0 and arr[i] not in even_val:
            even_val.append(arr[i])
    if len(even_val) == 0:
        return []
    return [min(even_val), even_val.index(min(even_val))]

# Time: O(n)
# Space: O(1)

# Optimized Solution

def pluck(arr):
    smallest_index = 0
    smallest_value = 2**31
    for i in range(len(arr)):
        if arr[i] % 2 == 0 and arr[i] < smallest_value:
            smallest_value = arr[i]
            smallest_index = i
    return [smallest_value, smallest_index]

# Time: O(n)
# Space: O(1)

```
pluck([4,2,3])   # [2, 1]
pluck([1,2,3])   # [2, 1]
pluck([])        # []
pluck([5, 0, 3, 0, 4, 2]) # [0, 1]
```
```

B:

```python

```

C:

```python

```

D:

```python

```

E:

```python

```

F:

```python

```

G:

```python

```

H:

```python

```

I:

```python

```

J:

```python

```

K:

```python

```

L:

```python

```

M:

```python

```

N:

```python

```

O:

```python

```

P:

```python

```

Q