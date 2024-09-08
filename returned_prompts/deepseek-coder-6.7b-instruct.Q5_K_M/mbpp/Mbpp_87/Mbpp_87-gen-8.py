
def merge_dictionaries_three(dict1, dict2, dict3):
    result = {}
    for d in (dict1, dict2, dict3):
        result.update(d)
    return result

dict1 = { "R": "Red", "B": "Black", "P": "Pink" }
dict2 = { "G": "Green", "W": "White" }
dict3 = { "O": "Orange", "W": "White", "B": "Black" }

print(merge_dictionaries_three(dict1, dict2, dict3))

"""
Output:
{'R': 'Red', 'B': 'Black', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
"""

"""
This function merges three dictionaries into one by iterating over the three dictionaries and updating the result dictionary with the content of each dictionary. If there are key collisions, the value from the last dictionary in the argument list takes precedence.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:
<jupyter_code>
