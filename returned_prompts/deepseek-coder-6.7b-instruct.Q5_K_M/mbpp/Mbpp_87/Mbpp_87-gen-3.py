
def merge_dictionaries_three(dict1, dict2, dict3):
    merged_dict = {**dict1, **dict2, **dict3}
    return merged_dict

print(merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" }))

"""
This function uses the ** operator to unpack the dictionaries and merge them. The values from the later dictionaries will overwrite the values of the earlier dictionaries if they have the same key.
"""

"""
This function will merge the three dictionaries into one, if the keys are the same in different dictionaries, the value from the later dictionary will overwrite the earlier one.
"""
<jupyter_output>
{'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
<jupyter_text>
