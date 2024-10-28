
def merge_dictionaries_three(dict1, dict2, dict3):
    merged_dict = {**dict1, **dict2, **dict3}
    return merged_dict
"""
This function uses the dictionary unpacking feature in Python 3.5 and later. It takes three dictionaries as inputs and returns a single dictionary that merges all of them. If there are any overlapping keys, the values from the second and third dictionaries will overwrite the values from the first dictionary.
"""

