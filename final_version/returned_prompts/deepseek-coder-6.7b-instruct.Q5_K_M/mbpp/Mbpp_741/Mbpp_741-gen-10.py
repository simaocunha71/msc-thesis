def all_Characters_Same(s: str):
    return len(set(s)) <= 1

print(all_Characters_Same("python"))  # False

"""
Explanation:
The function works by converting the string to a set. A set in python is an unordered collection of unique elements. When all characters are the same, all the characters will be identical and the set will only contain one element. If the string contains distinct characters, the set will contain more than one element. If the length of the set is less than or equal to 1, it means all the characters are the same.
"""

# --------

