
def search(lst):
    counter = {}
    for elem in lst:
        if elem in counter:
            counter[elem] += 1
        else:
            counter[elem] = 1
    for elem in counter:
        if counter[elem] >= elem:
            return elem
    return -1

# Time complexity: O(n)
# Space complexity: O(n)



```

```
def search(lst):
    freq_map = {}
    for elem in lst:
        freq_map[elem] = freq_map.get(elem, 0) + 1
    for elem in freq_map:
        if freq_map[elem] >= elem:
            return elem
    return -1
```

```
def search(lst):
    from collections import Counter
    return Counter(lst).most_common(1)[0][0] if any(i >= j for i, j in Counter(lst).items()) else -1
```

```
def search(lst):
    from collections import Counter
    return Counter(lst).most_common(1)[0][0] if any(i >= j for i, j in Counter(lst).most_common()) else -1
```

```
def search(lst):
    from collections import Counter
    return Counter(lst).most_common(1)[0][0] if Counter(lst).most_common(1)[0][1] >= Counter(lst).most_common(1)[0][0] else -1
```
```
```

```python
def search(lst):
    freq = {}
    for elem in lst:
        freq[elem] = freq.get(elem, 0) + 1
    for elem, f in freq.items():
        if f >= elem:
            return elem
    return -1
```
```python
def search(lst):
    freq = {}
    for elem in lst:
        freq[elem] = freq.get(elem, 0) + 1
    for elem in f