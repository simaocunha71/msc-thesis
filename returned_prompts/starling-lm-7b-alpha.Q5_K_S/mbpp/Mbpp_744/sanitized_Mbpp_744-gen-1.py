import sys
def check_none(tup):
    for i in tup:
        if i is None:
            return True
    return False
tup = (10, 4, 5, 6, None)