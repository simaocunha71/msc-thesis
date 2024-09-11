"""
def is_sublist(sublist, given_list):
    for i in range(len(given_list)-len(sublist)+1):
        if given_list[i:i+len(sublist)] == sublist:
            return True
    return False
"""

# Python3 program to check if a
# given list is a sublist of
# another list.

# Returns true if sublist
# is a sublist of given_list
def is_sublist(sublist, given_list):
    # length of sublist
    n = len(sublist)

    # traverse given_list and
    # check if all elements of
    # sublist are present in
    # given_list
    for i in range(len(given_list)):

        # If all elements of
        # sublist are present in
        # given_list
        if given_list[i:i + n] == sublist:
            return True

    return False

# Driver Program
print(is_sublist([2,4,3,5,7],[3,7]))











"""
def is_sublist(sublist, given_list):
    if len(sublist) > len(given_list):
        return False
    for i in range(len(given_list)):
        if given_list[i:i+len(sublist)] == sublist:
            return True
    return False
"""

"""
def is_sublist(sublist, given_list):
    if len(sublist) > len(given_list):
        return False
    for i in range(len(given_list)):
        if given_list[i:i+len(sublist)] == sublist:
            return True
    return False
"""

"""
def is_sublist(sublist, given_list):
    for i in range(len(given_list)):
        if given_list[i:i+len(sublist)] == sublist:
            return True
    return False
"""

"""
def is_sublist(sublist, given_list):
   