def merge_dictionaries_three(dict1, dict2, dict3):
    new_dict = dict1.copy()
    new_dict.update(dict2)
    new_dict.update(dict3)
    return new_dict


# Testing
print(merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" }))

# Expected output: {'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
"""
This function works by first creating a copy of the first dictionary. It then updates this copy by adding the key-value pairs from the second and third dictionaries. This ensures that the original dictionaries are not modified, while still returning a new dictionary that contains all of the key-value pairs from the three dictionaries.
"""




"""
The merge_dictionaries_three function takes three dictionaries as input and returns a new dictionary that contains all of the key-value pairs from the input dictionaries. It does this by creating a copy of the first dictionary and then updating this copy with the key-value pairs from the second and third dictionaries.

To test the function, you can call it with the example dictionaries provided in the assert statement: merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" }). This should return the expected output: {'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}.

The function ensures that the original dictionaries are not modified by creating a copy of the first dictionary. This is important because dictionaries in Python are mutable objects, meaning that any changes made to them are permanent and cannot be undone. By creating a copy, the function can safely