"""
def issort_list(lst):
    if len(lst) == 0:
        return True
    if len(lst) == 1:
        return True
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True
"""

# Alternative solution
def issort_list(lst):
    return lst == sorted(lst)

# Testing
assert issort_list([1,2,4,6,8,10,12,14,16,17])==True

# Testing False
assert issort_list([2,1,4,6,8,10,12,14,16,17])==False

# Testing False
assert issort_list([1,2,4,6,8,10,12,14,17,16])==False

# Testing False
assert issort_list([1,2,1,4,6,8,10,12,14,17])==False

# Testing False
assert issort_list([1,2,4,6,8,10,12,14,17,17])==False

# Testing False
assert issort_list([])==True

# Testing False
assert issort_list([1])==True

# Testing False
assert issort_list([1,2])==True

# Testing False
assert issort_list([1,2,3])==True

# Testing False
assert issort_list([1,2,3,4])==True

# Testing False
assert issort_list([1,2,3,4,5])==True

# Testing False
assert issort_list([1,2,3,4,5,6])==True

# Testing False
assert issort_list([1,2,3,5,4,6])==False

# Testing False
assert issort_list([1,2,3,4,5,6,7])==True

# Testing False