def interchange_safe(lst):
    for sublist in lst:
        if len(sublist) > 1:
            sublist[0], sublist[-1] = sublist[-1], sublist[0]
    return lst

print(interchange_safe([[12, 35, 9, 56, 24], [15], [1]]))

"""
Write a python function to interchange the first and last elements of all the sublists in a list of lists only if the sublist has more than one element and the length of the sublist is even.
assert interchange_safe_