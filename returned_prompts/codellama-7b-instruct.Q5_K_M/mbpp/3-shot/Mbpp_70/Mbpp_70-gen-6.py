
def get_equal(tups):
    length = len(tups[0])
    for tup in tups:
        if length != len(tup):
            return False
    return True


