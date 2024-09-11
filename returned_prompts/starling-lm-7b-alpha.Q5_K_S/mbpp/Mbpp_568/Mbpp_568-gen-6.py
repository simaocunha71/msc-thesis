"""
def empty_list(N):
    l=[]
    for i in range(N):
        l.append({})
    return l
"""

def empty_list(N):
    l=[]
    while len(l)!=N:
        l.append({})
    return l

assert empty_list(5)==[{},{},{},{},{}]

def empty_list(N):
    l=[]
    for _ in range(N):
        l.append({})
    return l

assert empty_list(5)==[{},{},{},{},{}]

def empty_list(N):
    l=[]
    for _ in range(N):
        l+={}
    return l

assert empty_list(5)==[{},{},{},{},{}]

def empty_list(N):
    l=[]
    while len(l)!=N:
        l.append({})
    return l

assert empty_list(5)==[{},{},{},{},{}]

def empty_list(N):
    l=[{}]*N
    return l

assert empty_list(5)==[{},{},{},{},{}]

def empty_list(N):
    return [dict() for _ in range(N)]

assert empty_list(5)==[{},{},{},{},{}]

def empty_list(N):
    l=[dict()] * N
    return l

assert empty_list(5)==[{},{},{},{},{}]

def empty_list(N):
    return [dict()] * N

assert empty_list(5)==[{},{},{},{},{}]

def empty_list(N):
    l=[dict()] * N
    return l

assert empty_list(5)==[{},{},{},{},{}]

def empty_list(N):
    l=[{}]*N
    return l

assert empty_list(5)==[{},{},{},{},{}]

def empty_list(N):
    l=[{}]*N
    return l

assert empty_list(5)==[{},{},{},{},{}]

def empty_list(N):
   