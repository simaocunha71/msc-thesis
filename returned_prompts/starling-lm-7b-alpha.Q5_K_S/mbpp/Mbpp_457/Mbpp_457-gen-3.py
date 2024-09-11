"""
def Find_Min(l):
    min_length = len(l[0])
    for i in range(len(l)):
        if len(l[i]) < min_length:
            min_length = len(l[i])
    for i in range(len(l)):
        if len(l[i]) == min_length:
            return l[i]

Find_Min([[1],[1,2],[1,2,3]])
"""

def Find_Min(l):
    return min(l, key = len)

Find_Min([[1],[1,2],[1,2,3]])


"""
def Find_Min(l):
    min_length = len(l[0])
    for i in range(len(l)):
        if len(l[i]) < min_length:
            min_length = len(l[i])
    for i in range(len(l)):
        if len(l[i]) == min_length:
            return l[i]

Find_Min([[1],[1,2],[1,2,3]])
"""

"""
def Find_Min(l):
    min_length = float('inf')
    for i in range(len(l)):
        if len(l[i]) < min_length:
            min_length = len(l[i])
    for i in range(len(l)):
        if len(l[i]) == min_length:
            return l[i]

Find_Min([[1],[1,2],[1,2,3]])
"""

"""
def Find_Min(l):
    min_length = len(l[0])
    for i in range(len(l)):
        if len(l[i]) < min_length:
            min_length = len(l[i])
    for i in range(len(l)):
        if len(l[i]) == min_length:
            return l[i]

Find_Min([[1],[1,2],[1,2,3]])
"""

"""
def Find_Min(l):
    min