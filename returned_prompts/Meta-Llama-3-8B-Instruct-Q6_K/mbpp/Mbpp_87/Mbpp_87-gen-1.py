```
def merge_dictionaries_three(dict1, dict2, dict3):
    merged_dict = {**dict1, **dict2, **dict3}
    return merged_dict
```


The function `merge_dictionaries_three` takes three dictionaries as input and returns a new dictionary that is the result of merging these three dictionaries. The `**` operator is used to unpack the key-value pairs from the input dictionaries into the new dictionary. If there are any duplicate keys, the value from the last dictionary will be used in the resulting dictionary. For example, in the unit test provided, the key "W" is present in both `dict2` and `dict3` with the value "White", but in the resulting dictionary, the value for "W" is "White" which is from `dict3`. 





Example usage:

```
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
```





This unit test checks that the function correctly merges the three dictionaries and handles duplicate keys. The expected output is a dictionary with all the key-value pairs from the input dictionaries, with the last value for each key being used in case of a duplicate key.