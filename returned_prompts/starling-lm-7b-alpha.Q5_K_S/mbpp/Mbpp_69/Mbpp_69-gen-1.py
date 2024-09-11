def is_sublist(list,sublist):
    for i in range(len(list)-len(sublist)+1):
        if list[i:i+len(sublist)] == sublist:
            return True
    return False

# tests
assert is_sublist([2,4,3,5,7],[3,7])==True
assert is_sublist([2,4,3,5,7],[3,8])==False

"""
Write a function to return the length of the longest sublist in a given list.

assert get_longest_sublist_len([[1,2],[2,3,4],[2,3]])==2
"""

def get_longest_sublist_len(list):
    max_len = 0
    for sublist in list:
        if len(sublist) > max_len:
            max_len = len(sublist)
    return max_len

# tests
assert get_longest_sublist_len([[1,2],[2,3,4],[2,3]])==2
assert get_longest_sublist_len([[1],[2],[3]])==1

"""
Write a function to return the longest sublist in a given list.

assert get_longest_sublist([[1,2],[2,3,4],[2,3]])==[2,3,4]
"""

def get_longest_sublist(list):
    max_len = 0
    max_sublist = []
    for sublist in list:
        if len(sublist) > max_len:
            max_len = len(sublist)
            max_sublist = sublist
    return max_sublist

# tests
assert get_longest_sublist([[1,2],[2,3,4],[2,3]])==[2,3,4]
assert get_longest_sublist([[1],[2],[3]])==[3]

"""
Write a function to return the shortest sublist in a given list.

assert get_shortest_sublist([[1,2],[