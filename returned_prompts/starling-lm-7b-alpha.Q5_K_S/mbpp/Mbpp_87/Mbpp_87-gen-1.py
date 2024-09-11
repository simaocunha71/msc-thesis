"""
def merge_dictionaries_three(d1, d2, d3):
    return {**d1, **d2, **d3}
"""

# In Python, you can merge 3 dictionaries into a single dictionary using the double asterisks operator (**). This is called unpacking a dictionary.
# The double asterisks operator is used to unpack the dictionaries d1, d2, and d3 into a new dictionary.
# This new dictionary will have all the key-value pairs of d1, d2, and d3, with any overlapping keys being resolved by taking the value from the last dictionary in the list (d3 in this case).
# Therefore, the function merge_dictionaries_three(d1, d2, d3) will return a dictionary that is a combination of d1, d2, and d3.

# Here is an example of how you can use the function:

# d1 = {"R": "Red", "B": "Black", "P": "Pink"}
# d2 = {"G": "Green", "W": "White"}
# d3 = {"O": "Orange", "W": "White", "B": "Black"}
# merged_dict = merge_dictionaries_three(d1, d2, d3)
# print(merged_dict)  # Output: {'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}

# The function merge_dictionaries_three(d1, d2, d3) takes three dictionaries as input and returns a single dictionary that is a combination of all three dictionaries.
# The function uses the double asterisks operator (**), which is used to unpack the dictionaries d1, d2, and d3 into a single dictionary.
# Any overlapping keys in the dictionaries are resolved by taking the value from the last dictionary in the list (d3 in this case).
# Therefore, the function merge_dictionaries_three(d1, d2, d3) will return a dictionary that is a combination of d1, d2, and d3.

# You can use the function by providing three