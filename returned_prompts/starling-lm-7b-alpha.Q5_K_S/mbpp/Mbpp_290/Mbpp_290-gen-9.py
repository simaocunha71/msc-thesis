"""
def max_length(lst):
    max_l = []
    for i in lst:
        if len(max_l) < len(i):
            max_l = i
    return (len(max_l), max_l)
"""

def max_length(lst):
    return max(lst, key=len)

assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
print("ok")




"""
"""

def max_length(lst):
    max_l = []
    for i in lst:
        if len(max_l) < len(i):
            max_l = i
    return (len(max_l), max_l)



assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
print("ok")



"""
"""

def max_length(lst):
    max_l = []
    for i in lst:
        if len(max_l) < len(i):
            max_l = i
    return (len(max_l), max_l)


assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
print("ok")
"""
"""


def max_length(lst):
    max_l = []
    for i in lst:
        if len(max_l) < len(i):
            max_l = i
    return (len(max_l), max_l)


assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3