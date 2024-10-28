def check_none(t):
    # Iterate through the tuple
    # and check for None
    for i in t:
        if i is None:
            return True
    return False