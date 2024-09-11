def merge_dictionaries_three(dict1, dict2, dict3):
    new_dict = {**dict1, **dict2, **dict3}
    return new_dict

# Test
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}

# Explanation
The function merge_dictionaries_three takes three dictionaries as input. Inside the function, the dictionaries are merged using the dictionary unpacking operator (**), which unpacks the dictionaries and merges them into a single dictionary. The merged dictionary is then returned. The test case checks if the function correctly merges the provided dictionaries into a single dictionary.

"""
"""

# Solution
def merge_dictionaries_three(dict1, dict2, dict3):
    new_dict = {**dict1, **dict2, **dict3}
    return new_dict

# Test
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}

# Explanation
The function merge_dictionaries_three takes three dictionaries as input. Inside the function, the dictionaries are merged using the dictionary unpacking operator (**), which unpacks the dictionaries and merges them into a single dictionary. The merged dictionary is then returned. The test case checks if the function correctly merges the provided dictionaries into a single dictionary.

"""

# Solution
def merge_dictionaries_three(dict1, dict2, dict3):
    new_dict = {