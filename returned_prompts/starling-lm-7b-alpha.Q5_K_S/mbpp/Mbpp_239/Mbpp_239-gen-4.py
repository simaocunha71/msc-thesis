```
def get_total_number_of_sequences(m, n):
    res = 0
    for i in range(1, m+1):
        res += max(0, (m//i) - (n-1))
    return res
```

Here is a function that generates all possible sequences with the conditions you provided. It uses a recursive approach to generate all possible sequences of length n, and then checks if each sequence meets the conditions.

```python
def generate_sequences(m, n, prev=None):
    if n == 0:
        return [[]]

    res = []
    for i in range(prev or 1, m+1):
        if i >= 2*prev and i <= m:
            for seq in generate_sequences(m, n-1, i):
                res.append([i] + seq)
    return res
```

Here is a function that checks if a given sequence of length n meets the conditions:

```python
def is_valid_sequence(m, seq, n):
    return all(i >= 2*prev and i <= m for i, prev in zip(seq, seq[1:]))
```

Here is a function that counts the number of valid sequences of length n that are less than or equal to m:

```python
def count_valid_sequences(m, n):
    res = 0
    for i in range(1, m+1):
        for seq in generate_sequences(m, n, i):
            if is_valid_sequence(m, seq, n):
                res += 1
    return res
```

Here is a function that finds the maximum length of a valid sequence of elements that are less than or equal to m:

```python
def max_sequence_length(m):
    res = 0
    for i in range(1, m+1):
        if is_valid_sequence(m, [i] * res, res+1):
            res += 1
    return res
```

Here is a function that finds the number of valid sequences of length n, where each element is greater than or equal to twice the