"""
def check_Consecutive(list):
    for i in range(len(list)-1):
        if list[i+1]-list[i]!=1:
            return False
    return True
"""

def check_Consecutive(list):
    return all(list[i+1]-list[i]==1 for i in range(len(list)-1))



"""
def check_Consecutive(list):
    for i in range(len(list)-1):
        if list[i+1]-list[i]!=1:
            return False
    return True
"""


"""
def check_Consecutive(list):
    for i in range(len(list)-1):
        if list[i+1]-list[i]!=1:
            return False
    return True
"""

assert check_Consecutive([1,2,3,4,5]) == True



# Other solutions
"""
def check_Consecutive(lst):
    lst = sorted(lst)
    return all(x == lst[0] + x for x in range(len(lst)))
"""
"""
def check_Consecutive(lst):
    lst = sorted(lst)
    return all(lst[i+1] == lst[i] + 1 for i in range(len(lst)-1))
"""

"""
def check_Consecutive(lst):
    lst.sort()
    return all(i == lst[0] + i for i in range(len(lst)))
"""

"""
def check_Consecutive(lst):
    lst.sort()
    return all(lst[i+1] == lst[i] + 1 for i in range(len(lst)-1))
"""

"""
def check_Consecutive(lst):
    if sorted(lst) == list(range(lst[0], lst[-1]+1)):
        return True
    return False
"""

"""
def check_Consecutive(lst):
    return all(lst[i+1] == lst[i] + 1 for i in range(len(