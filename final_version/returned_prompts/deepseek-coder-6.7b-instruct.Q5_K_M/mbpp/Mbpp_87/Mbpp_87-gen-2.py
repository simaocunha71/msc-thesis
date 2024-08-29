
def merge_dictionaries_three(dict1, dict2, dict3):
    merged_dict = {**dict1, **dict2, **dict3}
    return merged_dict

print(merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" }))

The function merge_dictionaries_three takes three dictionaries as arguments. It uses the dictionary unpacking feature of Python to merge the three dictionaries into a single dictionary. In the case where there are overlapping keys, the value from the third dictionary will be kept because it is the last dictionary in the unpacking operation. The merged dictionary is then returned.

In the given question, the last dictionary "{ "O": "Orange", "W": "White", "B": "Black" }" has a key "W" which is also in the first dictionary and the second dictionary. As per Python dictionary precedence, the value from the last dictionary will be kept. Hence, the value for the key "W" in the merged dictionary will be "White".
"""
"""

#Q2
"""
Write a function to merge two dictionaries into one, with values from the second dictionary overwriting values from the first if they have the same key.
assert merge_dictionaries({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" })=={'R': 'Red', 'B': 'Black', 'P': 'Pink', 'G': 'Green', 'W': 'White'}
"""

A2:

def merge_dictionaries(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

print(merge_dictionaries({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" }))

In the function merge_dictionaries, the dictionaries are merged using dictionary unpacking. In the case of overlapping keys, the values from the second dictionary will be used because they