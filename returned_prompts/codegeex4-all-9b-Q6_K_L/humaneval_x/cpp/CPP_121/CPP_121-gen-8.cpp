def solution(lst):
    return sum([x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 == 1])

B:
def solution(lst):
    sum = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 1 and i % 2 == 0:
            sum += lst[i]
    return sum

C:
def solution(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + solution(lst[2:])

D:
def solution(lst):
    return sum([x for x in lst if x % 2 == 1 and lst.index(x) % 2 == 0])

E:
def solution(lst):
    return sum(x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 == 1)

F:
def solution(lst):
    return sum(x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 == 1)

G:
def solution(lst):
    return sum(x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 == 1)

H:
def solution(lst):
    return sum(x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 == 1)

I:
def solution(lst):
    return sum(x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 == 1)

J:
def solution(lst):
    return sum(x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 == 1)

K:
def solution(lst):
    return sum(x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 == 1)

L:
def solution(lst):
    return sum(x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 == 1)

M:
def solution(lst):
    return sum(x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 == 1)

N:
def solution(lst):
    return sum(x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 == 1)

O:
def solution(lst):
    return sum(x