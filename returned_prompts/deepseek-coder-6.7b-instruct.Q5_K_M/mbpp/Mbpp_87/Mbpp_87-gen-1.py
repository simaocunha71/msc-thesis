Here is the Python code to solve the problem:

```python
def merge_dictionaries_three(dict1, dict2, dict3):
    result = {**dict1, **dict2, **dict3}
    return result

dict1 = { "R": "Red", "B": "Black", "P": "Pink" }
dict2 = { "G": "Green", "W": "White" }
dict3 = { "O": "Orange", "W": "White", "B": "Black" }

print(merge_dictionaries_three(dict1, dict2, dict3))
```

In this Python code, we are using a feature of Python called dictionary unpacking (`**` operator). It allows us to merge dictionaries in a single line of code. The order of dictionaries matters. Later dictionaries will overwrite keys in the previous dictionaries. In this case, the third dictionary `dict3` will overwrite the keys in the second dictionary `dict2`, and the second dictionary `dict2` will overwrite the keys in the first dictionary `dict1`.

The output of the code is:

```python
{'R': 'Red', 'B': 'Black', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
```

This is the merged dictionary.
"""

