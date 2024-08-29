def get_positive(l):
    return list(filter(lambda x: x > 0, l))

B:
def get_positive(l):
    return [x for x in l if x > 0]

C:
def get_positive(l):
    pos = []
    for i in l:
        if i > 0:
            pos.append(i)
    return pos

D:
def get_positive(l):
    pos = []
    for i in range(0, len(l)):
        if l[i] > 0:
            pos.append(l[i])
    return pos

E:
def get_positive(l):
    pos = []
    for i in range(len(l)-1, -1, -1):
        if l[i] > 0:
            pos.append(l[i])
    return pos

F:
def get_positive(l):
    pos = []
    for i in range(1, len(l)):
        if l[i] > 0:
            pos.append(l[i])
    return pos

G:
def get_positive(l):
    pos = []
    for i in range(0, len(l)):
        if l[i] < 0:
            pos.append(l[i])
    return pos

H:
def get_positive(l):
    pos = []
    for i in range(0, len(l)-1):
        if l[i] > 0:
            pos.append(l[i])
    return pos

I:
def get_positive(l):
    pos = []
    for i in range(len(l), 0, -1):
        if l[i] > 0:
            pos.append(l[i])
    return pos

J:
def get_positive(l):
    pos = []
    for i in range(len(l)):
        if l[i] < 0:
            pos.append(l[i])
    return pos

K:
def get_positive(l):
    pos = []
    for i in range(1, len(l)-1):
        if l[i] > 0:
            pos.append(l[i])
    return pos

L:
def get_positive(l):
    pos = []
    for i in range(len(l)-1, 0, -1):
        if l[i] > 0:
            pos.append(l[i])
    return pos

M:
def get_positive(l):
    pos = []
    for i in range(len(l)+1):
        if l[i] > 0:
            pos.append(l[i])
    return pos

N:
def get_positive(l):
    pos = []
    for i in range