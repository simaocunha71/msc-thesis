"""
def check_type(tup):
    #Check if the tuple is empty
    if not tup:
        return False

    #Check if all elements are of same type
    return all(type(tup[0]) == type(element) for element in tup)
"""
