"""
def remove_odd(lst):
    res = []
    for i in lst:
        if i % 2 == 0:
            res.append(i)
    return res
"""

#or

def remove_odd(lst):
    return [i for i in lst if i % 2 == 0]


"""
def remove_odd(lst):
    return [i for i in lst if i % 2 == 0]
"""

