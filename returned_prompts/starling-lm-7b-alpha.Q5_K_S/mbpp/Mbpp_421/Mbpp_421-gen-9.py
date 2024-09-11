def concatenate_tuple(t):
    return '-'.join(str(i) for i in t)

# assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'

"""
def concatenate_tuple(t):
    result = ""
    for i in t:
        result += str(i)
    return result

assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
"""

def concatenate_tuple(t):
    return '-'.join(map(str, t))

# assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'

"""
def concatenate_tuple(t):
    result = []
    for i in t:
        result.append(str(i))
    return '-'.join(result)

assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
"""

"""
def concatenate_tuple(t):
    result = ""
    for i in t:
        result += str(i)
    return result

# assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
"""


"""
def concatenate_tuple(t):
    return '-'.join(map(str, t))

# assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
"""


"""
def concatenate_tuple(t):
    result = []
    for i in t:
        result.append(str(i))
    return '-'.join(result)

# assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
"""


"""
def concatenate_tuple(t):
    result = ""
