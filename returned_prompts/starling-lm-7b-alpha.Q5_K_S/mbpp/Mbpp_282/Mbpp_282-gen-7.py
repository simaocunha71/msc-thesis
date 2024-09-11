def sub_list(list1,list2):
    # your code goes here
    l1 = len(list1)
    l2 = len(list2)
    if l1!=l2:
        return False
    for i in range(l1):
        if list1[i]-list2[i]!=0:
            return False
    return list1-list2

# Test
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]


"""
Write a function to add two lists element-wise.
assert add_list([1, 2, 3],[4,5,6])==[5,7,9]
"""
def add_list(list1,list2):
    # your code goes here
    l1 = len(list1)
    l2 = len(list2)
    if l1!=l2:
        return False
    for i in range(l1):
        if list1[i]+list2[i]!=0:
            return False
    return list1+list2

# Test
assert add_list([1, 2, 3],[4,5,6])==[5,7,9]

"""
Write a function to multiply two lists element-wise.
assert mul_list([1, 2, 3],[4,5,6])==[4,10,18]
"""
def mul_list(list1,list2):
    # your code goes here
    l1 = len(list1)
    l2 = len(list2)
    if l1!=l2:
        return False
    for i in range(l1):
        if list1[i]*list2[i]!=0:
            return False
    return list1*list2

# Test
assert mul_list([1, 2, 3],[4,5,6])==[4,10,18]

"""
Write a function to divide two lists element-wise.
assert div_list([1, 2, 3],[4,5,6])==[0.25, 0