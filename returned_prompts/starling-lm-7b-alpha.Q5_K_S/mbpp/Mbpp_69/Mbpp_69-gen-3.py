"""
def is_sublist(lst, sub_lst):
    if len(sub_lst) > len(lst):
        return False
    else:
        for i in range(len(lst)-len(sub_lst)+1):
            if lst[i:i+len(sub_lst)] == sub_lst:
                return True
    return False
"""

def is_sublist(lst, sub_lst):
    if len(sub_lst) > len(lst):
        return False
    else:
        for i in range(len(lst)-len(sub_lst)+1):
            if lst[i:i+len(sub_lst)] == sub_lst:
                return True
    return False


assert is_sublist([2,4,3,5,7],[3,7])==True
assert is_sublist([2,4,3,5,7],[3,4,7])==True
assert is_sublist([2,4,3,5,7],[3,7,6])==False
assert is_sublist([2,4,3,5,7],[3,7])==True
assert is_sublist([],[1])==False
assert is_sublist([],[])==True
assert is_sublist([3,3,3],[3,3])==True
assert is_sublist([3,3,3],[3])==True
assert is_sublist([3,3,3],[3,3,3])==True
assert is_sublist([3,3,3],[3,3,4])==False

"""
"""
def is_sublist(lst, sub_lst):
    if len(sub_lst) > len(lst):
        return False
    else:
        for i in range(len(lst)-len(sub_lst)+1):
            if lst[i:i+len(sub_lst)] == sub_lst:
                return True
    return False
"""

def is_sublist(lst, sub_lst):
    if len(sub_lst) > len(lst):
        return False
    else:
        for i in