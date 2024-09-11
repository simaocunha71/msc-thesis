Here's one way you could do it:

```python
def pack_consecutive_duplicates(l):
    result = []
    prev = None
    count = 0
    for elem in l:
        if elem == prev:
            count += 1
        else:
            if count > 0:
                result.append([prev] * count)
            count = 1
        prev = elem
    if count > 0:
        result.append([prev] * count)
    return result
```

Here's an explanation of how it works:

- `prev` keeps track of the previous element we've seen.
- `count` keeps track of how many consecutive duplicates we've seen.
- We loop over the input list. For each element:
  - If it's the same as the previous element, we increment the count.
  - If it's different from the previous element, we add a sublist to the result containing the previous element repeated `count` times. Then we reset the count to 1.
- After the loop, we add a sublist to the result containing the previous element repeated `count` times, in case there were no duplicates at all.

Here's an interactive example you can play with:

```python
def pack_consecutive_duplicates(l):
    result = []
    prev = None
    count = 0
    for elem in l:
        if elem == prev:
            count += 1
        else:
            if count > 0:
                result.append([prev] * count)
            count = 1
        prev = elem
    if count > 0:
        result.append([prev] * count)
    return result

# Test cases:
print(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))  # [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [