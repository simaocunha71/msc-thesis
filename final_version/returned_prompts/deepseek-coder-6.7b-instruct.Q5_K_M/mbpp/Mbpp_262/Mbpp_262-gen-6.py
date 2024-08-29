
def split_two_parts(lst, l):
    return lst[:l], lst[l:]

print(split_two_parts([1,1,2,3,4,4,5,1],3))

"""
Output:
([1, 1, 2], [3, 4, 4, 5, 1])
"""

