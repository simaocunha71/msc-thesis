def check_occurences(my_list):
    new_dict = {}
    for item in my_list:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    return new_dict

# Test
print(check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]))












"""
def check_occurences(my_list):
    new_dict = {}
    for item in my_list:
        if item not in new_dict:
            new_dict[item] = 1
        else:
            new_dict[item] += 1
    return new_dict
"""

# Test
print(check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]))
"""
def check_occurences(my_list):
    new_dict = {}
    for item in my_list:
        if item not in new_dict:
            new_dict[item] = 0
        new_dict[item] += 1
    return new_dict
"""
# Test
print(check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]))


```