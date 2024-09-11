def reverse_string_list(list):
    return [item[::-1] for item in list]

reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])



"""
def reverse_string_list(list):
    list_rev = []
    for item in list:
        list_rev.append(item[::-1])
    return list_rev

reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])
"""


"""
def reverse_string_list(list):
    list_rev = []
    for item in list:
        list_rev.append(item)
        list_rev[-1] = list_rev[-1][::-1]
    return list_rev

reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])
"""

"""
def reverse_string_list(list):
    list_rev = []
    for item in list:
        list_rev.append(item)
        item = item[::-1]
    return list_rev

reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])
"""


"""
def reverse_string_list(list):
    list_rev = []
    for item in list:
        item = item[::-1]
        list_rev.append(item)
    return list_rev

reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])
"""


"""
def reverse_string_list(list):
    list_rev = []
    for item in list:
        item = item[::-1]
        list_rev.insert(0,item)
    return list_rev

reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])
"""

"""
def reverse_string_list(list):
    list_rev = []
    for item in list:
        item = item[::-1]
        list_rev.append(item)
        list_rev.insert(0,item)
    return list_rev

reverse_string_