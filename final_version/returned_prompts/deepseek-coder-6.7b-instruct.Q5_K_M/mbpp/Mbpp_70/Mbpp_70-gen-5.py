
def get_equal(tup):
    len_list = [len(i) for i in tup]
    return len_list.count(len_list[0]) == len(len_list)

print(get_equal([(11, 22, 33),  (44,_55, 66)]))

"""
Here, we use a list comprehension to create a list of lengths of the tuples. Then, we check whether all the elements in the list are the same (i.e., all the tuples have the same length). If they are the same, we return True; otherwise, we return False.
"""

