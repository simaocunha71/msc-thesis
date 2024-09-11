def frequency_lists(l):
    freq = {}
    for i in l:
        for j in i:
            if j not in freq:
                freq[j] = 1
            else:
                freq[j] += 1
    return freq





# Made By Mostafa_Khaled
```

```
from collections import defaultdict

def frequency_lists(l):
    freq = defaultdict(int)
    for i in l:
        for j in i:
            freq[j] += 1
    return freq
```
```
```

```python
# Made By Mostafa_Khaled

def frequency_lists(l):
    freq = {}
    for i in l:
        for j in i:
            if j not in freq:
                freq[j] = 1
            else:
                freq[j] += 1
    return freq
```

```
```

```python
def frequency_lists(l):
    freq = {}
    for i in l:
        for j in i:
            if j not in freq:
                freq[j] = 1
            else:
                freq[j] += 1
    return freq
```
```
```

```python
from collections import Counter
def frequency_lists(l):
    freq = Counter()
    for i in l:
        for j in i:
            freq[j] += 1
    return freq
```
```
```

```python
def frequency_lists(l):
    freq = {}
    for i in l:
        for j in i:
            if j not in freq:
                freq[j] = 1
            else:
                freq[j] += 1
    return freq
```
```
```

```python
def frequency_lists(l):
    freq = {}
    for i in l:
        for j in i:
           