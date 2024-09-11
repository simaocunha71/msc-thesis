"""
def get_equal(tup_list):
    for i in range(len(tup_list)):
        if len(tup_list[i]) != len(tup_list[0]):
            return False
    return True
"""

from collections import Counter

def get_equal(tup_list):
    return Counter(len(t) for t in tup_list).most_common()[0][0] == len(tup_list[0])





"""
def get_equal(tup_list):
    if all(len(tup_list[i]) == len(tup_list[0]) for i in range(len(tup_list))):
        return True
    else:
        return False
"""


"""
def get_equal(tup_list):
    if len(set(map(len, tup_list))) == 1:
        return True
    else:
        return False
"""

"""
def get_equal(tup_list):
    if all(len(tup) == len(tup_list[0]) for tup in tup_list):
        return True
    else:
        return False
"""

"""
def get_equal(tup_list):
    if len(tup_list) == 0:
        return True
    if len(tup_list) == 1:
        return True
    if len(tup_list) == 2:
        if len(tup_list[0]) == len(tup_list[1]):
            return True
        else:
            return False
    else:
        return False
"""

"""
def get_equal(tup_list):
    if len(tup_list) > 2:
        return False
    if len(tup_list) == 0:
        return True
    if len(tup_list) == 1:
        return True
    if len(tup_list) == 2:
        if len(tup_list[0]) == len(tup_list[1]):
            return True
        else:
