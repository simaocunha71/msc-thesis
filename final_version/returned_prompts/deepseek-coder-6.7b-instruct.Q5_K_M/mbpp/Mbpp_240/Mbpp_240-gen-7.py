def replace_list(list1, list2):
    list1.pop()
    list1.extend(list2)
    return list1

print(replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8]))

# OR

def replace_list(list1, list2):
    list1[-1:] = list2
    return list1

print(replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8]))

# OR

def replace_list(list1, list2):
    list1.remove(list1[-1])
    list1.extend(list2)
    return list1

print(replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8]))

# OR

def replace_list(list1, list2):
    list1 = list1[:-1] + list2
    return list1

print(replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8]))

# OR

def replace_list(list1, list2):
    list1[len(list1)-1:] = list2
    return list1

print(replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8]))

All of these methods will return the same output:
[1, 3, 5, 7, 9, 2, 4, 6, 8]
"""

# OR

def replace_list(list1, list2):
    list1[-1:] = list2
    return list1

print(replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8]))

# OR

def replace_list(list1, list2):
    list1.remove(list1[-1