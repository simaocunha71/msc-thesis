def merge_dictionaries_three(dict1, dict2, dict3):
    return {**dict1, **dict2, **dict3}

dict1 = { "R": "Red", "B": "Black", "P": "Pink" }
dict2 = { "G": "Green", "W": "White" }
dict3 = { "O": "Orange", "W": "White", "B": "Black" }

print(merge_dictionaries_three(dict1, dict2, dict3))

# Output: {'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}

"""
The function `merge_dictionaries_three` uses the `**` operator to unpack the dictionaries and merge them into a new dictionary.
If there are any overlapping keys, the value from the last dictionary to be unpacked will overwrite the value from the previous dictionaries.
"""

"""
You can also use the `update()` method:

def merge_dictionaries_three(dict1, dict2, dict3):
    dict1.update(dict2)
    dict1.update(dict3)
    return dict1
"""

"""
Both of these solutions will give the same result. The choice between the two depends on your preference and what you are more comfortable with.
"""

"""
In Python 3.5 and later versions, you can use the `{**a, **b}` syntax for the same effect.
"""

"""
Note: If the dictionaries have the same key but different values, the value from the last dictionary will overwrite the value from the previous dictionaries. If you want to keep all values, you will need to handle that case yourself.
"""

"""
If the dictionaries have the same key and you want to combine their values, you can use a list as the value:

def merge_dictionaries_three(dict1, dict2, dict3):
    result = {}
    for d in (dict1, dict2, dict3):
        for k, v in d.items():
            if k in result:
                result[k].append(v)
            else