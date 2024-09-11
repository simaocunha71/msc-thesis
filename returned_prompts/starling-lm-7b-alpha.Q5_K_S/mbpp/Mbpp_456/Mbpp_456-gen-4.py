def reverse_string_list(list_strings):
    list_strings = [list_strings[i][::-1] for i in range(len(list_strings))]
    return list_strings


def test_reverse_string_list():
    assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']


test_reverse_string_list()


# def reverse_string_list(list_strings):
#     for i in range(len(list_strings)):
#         list_strings[i] = list_strings[i][::-1]
#     return list_strings





# def test_reverse_string_list():
#     assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']


# test_reverse_string_list()


"""
def reverse_list(list_strings):
    list_strings = [list_strings[i][::-1] for i in range(len(list_strings))]
    return list_strings
"""

# def test_reverse_list():
#     assert reverse_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']


# test_reverse_list()

# def reverse_list(list_strings):
#     for i in range(len(list_strings)):
#         list_strings[i] = list_strings[i][::-1]
#     return list_strings


# def test_reverse_list():
#     assert reverse_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']


# test_reverse_list()

"""
def reverse_list(list_strings):
    for i in range(len(list