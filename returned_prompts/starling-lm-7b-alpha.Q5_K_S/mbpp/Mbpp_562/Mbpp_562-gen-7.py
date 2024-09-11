"""
def Find_Max_Length(l):
    Max = 0
    for i in range(len(l)):
        if len(l[i]) > Max:
            Max = len(l[i])
    return Max
"""

def Find_Max_Length(l):
    return max(map(len, l))

assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4





def Find_Max_Length(l):
    max_length = 0
    for sublist in l:
        current_length = len(sublist)
        if current_length > max_length:
            max_length = current_length
    return max_length





"""
def Find_Max_Length(l):
    Max = 0
    for i in range(len(l)):
        if len(l[i]) > Max:
            Max = len(l[i])
    return Max
"""

def Find_Max_Length(l):
    return max(map(len, l))

assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4





def Find_Max_Length(l):
    max_length = 0
    for sublist in l:
        current_length = len(sublist)
        if current_length > max_length:
            max_length = current_length
    return max_length





"""
def Find_Max_Length(l):
    Max = 0
    for i in range(len(l)):
        if len(l[i]) > Max:
            Max = len(l[i])
    return Max
"""

def Find_Max_Length(l):
    return max(map(len, l))

assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4





def Find_Max_Length(l):
    max_length = 0
    for sublist in l:
        current_length = len(sublist)
