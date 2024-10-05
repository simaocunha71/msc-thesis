
def histogram(test):
    d = {}
    for i in test:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    max_count = max(d.values())
    max_keys = [k for k, v in d.items() if v == max_count]
    return {k: v for k, v in d.items() if v == max_count}
```


```python
def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') ==