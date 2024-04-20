"""
Write a function takes as input two lists [a_1,...,a_n], [b_1,...,b_n] and returns [a_1+b_1,...,a_n+b_n].
assert sum_list([10,20,30],[15,25,35])==[25,45,65]
"""

def add_lists(a_list, b_list):
    res = list()
    for i in range(len(b_list)):
        res.append(sum_list([a_list], [b_list]))
    return res
