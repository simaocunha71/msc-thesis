def get_positive(l):
    return list(filter(lambda x: x>0, l))

B:
def get_positive(l):
    return [x for x in l if x>0]

C:
def get_positive(l):
    for i in range(len(l)):
        if l[i] < 0:
            del l[i]
    return l

D:
def get_positive(l):
    for i in l:
        if i < 0:
            l.remove(i)
    return l

E:
def get_positive(l):
    return l.index(l>0)

F:
def get_positive(l):
    return filter(lambda x: x>0, l)

G:
def get_positive(l):
    for i in range(len(l)):
        if l[i] < 0:
            l.pop(i)
    return l

H:
def get_positive(l):
    for i in range(len(l)):
        if l[i] < 0:
            l.remove(i)
    return l

I:
def get_positive(l):
    return l.pop(l>0)

J:
def get_positive(l):
    for i in l:
        if i < 0:
            l.remove(i)
    return filter(lambda x: x>0, l)

K:
def get_positive(l):
    for i in range(len(l)):
        if l[i] > 0:
            l.pop(i)
    return l

L:
def get_positive(l):
    for i in l:
        if i > 0:
            return i

M:
def get_positive(l):
    for i in range(len(l)):
        if l[i] > 0:
            return i

N:
def get_positive(l):
    return l.index(l>0)

O:
def get_positive(l):
    for i in l:
        if i > 0:
            l.remove(i)
    return l

P:
def get_positive(l):
    for i in l:
        if i < 0:
            l.remove(i)
    return filter(lambda x: x>0, l)

