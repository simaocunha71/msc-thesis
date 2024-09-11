def merge_dictionaries_three(dict1, dict2, dict3):
    result = {}
    result.update(dict1)
    result.update(dict2)
    result.update(dict3)
    return result

# Test
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}






"""
Given a string, return the length of the longest substring that contains all of the specified characters.

For example:
assert longest_substring('abcabcbb', 'b') == 2
assert longest_substring('pwwkew', 'kew') == 3

In the first example, the longest substring containing all characters of 'b' is "abc". In the second example, the longest substring is "wke".
"""


def longest_substring(string, sub):
    longest_length = 0
    sub_index = 0
    for i in range(len(string)):
        if string[i] not in sub:
            sub_index = i + 1
            break
    for i in range(sub_index, len(string)):
        if string[i] in sub:
            longest_length = max(longest_length, i - sub_index + 1)
        else:
            sub_index = i + 1
    return longest_length

# Test
assert longest_substring('abcabcbb', 'b') == 2
assert longest_substring('pwwkew', 'kew') == 3






"""
Return a new dictionary that contains all the keys and values from the original dictionary, but with all the keys sorted in ascending order by the value.

For example:
assert sort_dict({ "b": 1, "a": 2, "c": 3 }) == { "b": 1, "