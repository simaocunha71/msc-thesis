```
def merge_dictionaries_three(dict1, dict2, dict3):
    merged = dict1.copy()
    merged.update(dict2)
    merged.update(dict3)
    return merged
```
This function takes three dictionaries as input and returns a new dictionary that is the result of merging the three input dictionaries. It uses the `copy` and `update` methods of the dictionary to achieve this.

The unit test `assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}` shows that the function correctly merges the three input dictionaries. If there are duplicate keys, the function will use the value from the last dictionary. In this case, the key "W" is present in both the second and third dictionaries, and the function uses the value "White" from the third dictionary. The key "B" is also present in both the second and third dictionaries, and the function uses the value "Black" from the third dictionary. The resulting dictionary has all the key-value pairs from the three input dictionaries.