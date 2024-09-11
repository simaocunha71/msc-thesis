def concatenate_tuple(tup):
    return "-".join(tup)

# assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'



"""
The above function will fail if the tuple contains non-string values.
To make it work for all types of data, you can use the following code:
"""

def concatenate_tuple(tup):
    return "-".join(str(i) for i in tup)

# assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'


"""
Note:
The above function will also fail if the tuple is empty.
To make it work for empty tuples as well, you can use the following code:
"""

def concatenate_tuple(tup):
    if len(tup) == 0:
        return ""
    return "-".join(str(i) for i in tup)

# assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
# assert concatenate_tuple(tuple()) == ""
"""
Note:
The above function will also fail if the tuple contains None values.
To make it work for None values as well, you can use the following code:
"""

def concatenate_tuple(tup):
    if len(tup) == 0:
        return ""
    tup = tuple(filter(lambda x: x is not None, tup))
    return "-".join(str(i) for i in tup)

# assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
# assert concatenate_tuple(tuple()) == ""
# assert concatenate_tuple((None,)) == ""
"""
Note:
The above function will also fail if the tuple contains non-hashable values.
To make it work for all types of data, you can use the following code:
"""

def concatenate_tuple(tup