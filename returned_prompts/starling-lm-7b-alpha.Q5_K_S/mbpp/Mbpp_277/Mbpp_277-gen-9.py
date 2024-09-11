```python
def dict_filter(dictionary, n):
    res = {}
    for key, value in dictionary.items():
        if value >= n:
            res[key