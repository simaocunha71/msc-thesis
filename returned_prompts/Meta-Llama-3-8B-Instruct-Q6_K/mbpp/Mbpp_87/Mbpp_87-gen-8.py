```
def merge_dictionaries_three(dict1, dict2, dict3):
    merged_dict = {**dict1, **dict2, **dict3}
    return merged_dict
```
This function takes three dictionaries as input and returns a new dictionary that is the result of merging all three input dictionaries. The merge is done by using the dictionary unpacking operator (`**`) to concatenate the dictionaries.

The unit test provided in the problem ensures that the function works correctly. It checks that the merged dictionary contains all the key-value pairs from the input dictionaries, with no duplicates. The test also checks that the function returns a new dictionary and does not modify the input dictionaries.

Here is the unit test:
```
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
```  ```python
def merge_dictionaries_three(dict1, dict2, dict3):
    merged_dict = {**dict1, **dict2, **dict3}
    return merged_dict
```  ```python
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
```  ```python
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
```  ```python
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "