def concatenate_tuple(t):
    t_str = ''
    for i in t:
        t_str += str(i) + '-'
    return t_str[:-1]

# Test
print(concatenate_tuple(("ID", "is", 4, "UTS")))  # 'ID-is-4-UTS'
# Test
print(concatenate_tuple(("id", "isn't", 3, "UTS")))  # 'id-isn't-3-UTS'
# Test
print(concatenate_tuple(("id", "isn't", 3.0, "UTS")))  # 'id-isn't-3-UTS'
# Test
print(concatenate_tuple(("id", "isn't", 3, "UTS", 5)))  # 'id-isn't-3-UTS-5'
# Test
print(concatenate_tuple(()))  # ''


"""
Run time error
"""


def concatenate_tuple(t):
    t_str = ''
    for i in t:
        t_str += str(i) + '-'
    return t_str[:-1]

# Test
print(concatenate_tuple(("id", "isn't", 3, "UTS")))  # 'id-isn't-3-UTS'
# Test
print(concatenate_tuple(("id", "isn't", 3.0, "UTS")))  # 'id-isn't-3-UTS'
# Test
print(concatenate_tuple(("id", "isn't", 3, "UTS", 5)))  # 'id-isn't-3-UTS-5'
# Test
print(concatenate_tuple(()))  # ''

# Test
print(concatenate_tuple((4, "UTS")))  # '4-UTS'
# Test
print(concatenate_tuple((4, "UTS", "")))  # '4-UTS-'
