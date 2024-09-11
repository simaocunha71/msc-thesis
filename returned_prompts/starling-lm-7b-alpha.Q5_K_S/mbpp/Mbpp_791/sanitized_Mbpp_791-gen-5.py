def remove_nested(t):
    # Convert the tuple to a list to make it easier to remove elements
    l = list(t)
    # Iterate through the list and remove any sublists
    for i in range(len(l)):
        if isinstance(l[i], tuple):
            del l[i]
    # Convert the list back to a tuple
    return tuple(l)