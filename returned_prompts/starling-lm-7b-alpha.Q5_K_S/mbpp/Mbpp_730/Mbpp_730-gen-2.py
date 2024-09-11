def consecutive_duplicates(lst):
    lst_new = []
    for i in range(len(lst)):
        if i == 0:
            lst_new.append(lst[i])
        else:
            if lst[i] != lst[i-1]:
                lst_new.append(lst[i])
    return lst_new

# Test
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
print("All Tests Passed")



"""
A
"""


































"""
def consecutive_duplicates(lst):
    new_list = []
    for i in range(len(lst)):
        if i == 0:
            new_list.append(lst[i])
        elif lst[i] != lst[i-1]:
            new_list.append(lst[i])
    return new_list

assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
print("All Tests Passed")
"""

"""

"""
def consecutive_duplicates(lst):
    new_list = []
    for i in range(len(lst)):
        if i == 0:
            new_list.append(lst[i])
        elif lst[i] != lst[i-1]:
            new_list.append(lst[i])
    return new_list

assert consecutive_du