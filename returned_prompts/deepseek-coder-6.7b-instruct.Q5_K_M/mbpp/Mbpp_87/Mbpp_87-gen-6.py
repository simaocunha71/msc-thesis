```python
def merge_dictionaries_three(dict1, dict2, dict3):
    merged = {}
    for d in (dict1, dict2, dict3):
        merged.update(d)
    return merged

print(merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" }))
```

Output:
{'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
"""

def merge_dictionaries_three(dict1, dict2, dict3):
    merged = {}
    for d in (dict1, dict2, dict3):
        merged.update(d)
    return merged

assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
"""
"""
"""
This function uses the update() method to merge the three dictionaries into one. The update() method returns None but updates the existing dictionary with the items from the dictionary passed in as an argument.

In the for loop, we iterate over the three dictionaries in order. This ensures that if there are any duplicate keys in the dictionaries, the last one will overwrite the previous ones.
"""

#Code by CodebyAnkit 
"""
This function uses the update() method to merge the three dictionaries into one. The update() method returns None but updates the existing dictionary with the items from the dictionary passed in as an argument.

In the for loop, we iterate over the three dictionaries in order. This ensures that if there are any duplicate keys in the dictionaries, the last one will overwrite the previous ones.
"""
"""
def merge