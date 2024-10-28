def sample_nam(names):
    """
    Sum the length of the names of a given list of names after removing the names that start with a lowercase letter.
    """
    total_length = 0
    for name in names:
        if name[0].isupper():
            total_length += len(name)
    return total_length