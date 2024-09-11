"""
def min_val(lst):
    return min(lst)
"""

def min_val(lst):
    return min(lst)


print(min_val(['Python', 3, 2, 4, 5, 'version']))






"""

def min_val(lst):
    min_num = lst[0]
    for i in range(1,len(lst)):
        if lst[i] < min_num:
            min_num = lst[i]
    return min_num

print(min_val(['Python', 3, 2, 4, 5, 'version']))




def min_val(lst):
    return sorted(lst)[0]

print(min_val(['Python', 3, 2, 4, 5, 'version']))


"""




"""

def min_val(lst):
    for i in lst:
        if type(i) == int:
            return i

print(min_val(['Python', 3, 2, 4, 5, 'version']))

"""





"""
def min_val(lst):
    min_num = lst[0]
    for i in range(len(lst)):
        if type(lst[i]) == int:
            if lst[i] < min_num:
                min_num = lst[i]
    return min_num

print(min_val(['Python', 3, 2, 4, 5, 'version']))

"""

def min_val(lst):
    min_num = lst[0]
    for i in range(len(lst)):
        if lst[i] < min_num:
            min_num = lst[i]
    return min_num

print(min_val(['Python', 3, 2, 4, 5, 'version']))







"""
def min_val(lst):
    min_num = lst[0]
    for i in range(len(lst)):
       