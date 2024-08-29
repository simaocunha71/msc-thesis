```python
def drop_empty(dic):
    return {k: v for k, v in dic.items() if v is not None}

print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None}))
```

Output:
```python
{'c1': 'Red', 'c2': 'Green'}
```

Explanation:
The function `drop_empty` is using dictionary comprehension to create a new dictionary. The condition `if v is not None` is used to only include items in the new dictionary if their value is not None.
"""

