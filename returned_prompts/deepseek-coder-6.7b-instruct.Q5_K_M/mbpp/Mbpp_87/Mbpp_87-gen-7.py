
def merge_dictionaries_three(dict1, dict2, dict3):
    merged = {**dict1, **dict2, **dict3}
    return merged

dict1 = { "R": "Red", "B": "Black", "P": "Pink" }
dict2 = { "G": "Green", "W": "White" }
dict3 = { "O": "Orange", "W": "White", "B": "Black" }
print(merge_dictionaries_three(dict1, dict2, dict3))

# Output: {'R': 'Red', 'B': 'Black', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}

"""
In the function merge_dictionaries_three, three dictionaries are merged using the ** operator. The ** operator is used to unpack the dictionaries into the merged dictionary. If there are any duplicate keys, the value from the last dictionary will overwrite the previous ones.
"""

#end