Here is a solution to the problem:

```python
def encode_cyclic(s):
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    groups2 = []
    for group in groups:
        if len(group) == 3:
            groups2.append(group[1:] + group[0])
        else:
            groups2.append(group)
    return ''.join(groups2)

def decode_cyclic(s):
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    groups2 = []
    for group in groups:
        if len(group) == 3:
            groups2.append(group[-1] + group[:-1])
        else:
            groups2.append(group)
    return ''.join(groups2)
```

The `encode_cyclic` function splits the input string into groups of three characters, and then rotates each group by moving the first character to the end. The `decode_cyclic` function does the opposite operation, rotating each group by moving the last character to the front.