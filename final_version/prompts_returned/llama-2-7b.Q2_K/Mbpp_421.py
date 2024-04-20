"""
Write a function to concatenate each element of tuple by the delimiter.
assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
"""

def concatenate_tuple(tuple):
    """
    Args:
       tuple (list)
    Return Value:
        str value of tuples
    Example:
        concatenate_tuple(("ID", "is", 4, "UTS"))
    """
    result = ""
    for e in tuple:
        if not type(e).__name__=="str":
            raise TypeError('The first element of the tuples ' +
                            'should be str or bytes.')

    # convert each element to string
    for elem in tuple:
        result += str(elem) + ','

    return result[:-1]

if __name__ == "__main__":
    print("concatenate_tuple() - Example Call")
    print(concatenate_tuple(['ID', 'is', 4, 'UTS']))
