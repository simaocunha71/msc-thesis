def issort_list(lst):
    return lst == sorted(lst)

print(issort_list([1,2,4,6,8,10,12,14,16,17])) # should return True

"""
This function works by comparing the original list to a sorted version of the list. If they are the same, then the original list was sorted, and the function returns True. Otherwise, it returns False.
"""

"""
Test Case 2:
"""

