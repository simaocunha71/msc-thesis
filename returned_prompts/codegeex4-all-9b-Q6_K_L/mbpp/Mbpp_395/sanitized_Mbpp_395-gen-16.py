def first_non_repeating_character(string):
    from collections import OrderedDict
    char_dict = OrderedDict()
    for char in string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    for char in char_dict:
        if char_dict[char] == 1:
            return char
    return None