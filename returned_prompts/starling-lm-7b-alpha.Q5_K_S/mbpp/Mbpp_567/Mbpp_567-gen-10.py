def issort_list(l):
    for i in range(1,len(l)):
        if l[i]<l[i-1]:
            return False
    return True



"""
def issort_list(l):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            return False
    return True
"""





"""
def issort_list(l):
    for i in range(len(l)-1):
        if l[i+1]-l[i]!=1:
            return False
    return True
"""

"""
def issort_list(l):
    if l[-1]>=l[0]:
        return True
    else:
        return False
"""

"""
def issort_list(l):
    for i in range(len(l)-1):
        if l[i]>=l[i+1]:
            return False
    return True
"""

"""
def issort_list(l):
    for i in range(len(l)-1):
        if l[i]<l[i+1]:
            return True
    return False
"""

"""
def issort_list(l):
    for i in range(len(l)-1):
        if l[i+1]-l[i]!=1:
            return False
    return True
"""

"""
def issort_list(l):
    for i in range(len(l)-1):
        if l[i]!=l[i+1]:
            return False
    return True
"""

"""
def issort_list(l):
    for i in range(len(l)-1):
        if l[i]<l[i+1]:
            return True
    return False
"""



assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
assert issort_list([1,2,3,5,6,7,8,10])==False
assert issort_list([1,2,3,5,6