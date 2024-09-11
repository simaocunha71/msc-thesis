"""
def is_sublist(mainlist,sublist):
    for i in range(len(mainlist)-len(sublist)+1):
        if mainlist[i:i+len(sublist)]==sublist:
            return True
    return False

print(is_sublist([2,4,3,5,7],[3,7]))
"""


def is_sublist(mainlist,sublist):
    return sublist in mainlist

print(is_sublist([2,4,3,5,7],[3,7]))



"""
def is_sublist(mainlist,sublist):
    if len(mainlist)<len(sublist):
        return False
    else:
        for i in range(len(mainlist)-len(sublist)+1):
            if mainlist[i:i+len(sublist)]==sublist:
                return True
    return False

print(is_sublist([2,4,3,5,7],[3,7]))
"""



"""
def is_sublist(mainlist,sublist):
    if len(mainlist)<len(sublist):
        return False
    else:
        for i in range(len(mainlist)-len(sublist)+1):
            if mainlist[i:i+len(sublist)]==sublist:
                return True
    return False

print(is_sublist([2,4,3,5,7],[3,7]))
"""



"""
def is_sublist(mainlist,sublist):
    if len(mainlist)<len(sublist):
        return False
    else:
        for i in range(len(mainlist)-len(sublist)+1):
            if mainlist[i:i+len(sublist)]==sublist:
                return True
    return False

print(is_sublist([2,4,3,5,7],[3,7]))
"""


"""
def is_sublist(mainlist,sublist):
    if len(mainlist)<len(sublist):
        return False
    else:
