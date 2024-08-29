def remove_elements(l1, l2):
    for i in l2:
        while i in l1:
            l1.remove(i)
    return l1

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))

# OR

def remove_elements(l1, l2):
    return [i for i in l1 if i not in l2]

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))

# OR

def remove_elements(l1, l2):
    return list(set(l1) - set(l2))

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))

# OR

def remove_elements(l1, l2):
    return list(filter(lambda x: x not in l2, l1))

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))

# OR

def remove_elements(l1, l2):
    return list(numpy.setdiff1d(l1, l2))

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))

"""
In all cases, it will return [1, 3, 5, 7, 9, 10] which are the elements present in the first list but not in the second.
"""
<jupyter_output>
[1, 3, 5, 7, 9, 10]
[1, 