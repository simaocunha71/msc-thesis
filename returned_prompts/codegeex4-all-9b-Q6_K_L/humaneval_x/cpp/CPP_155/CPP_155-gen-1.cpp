def even_odd_count(num):
    return [num.count('0'), num.count('1')]

B:
def even_odd_count(n):
    n = str(abs(n))
    return [sum(1 for i in n if int(i) % 2 == 0), sum(1 for i in n if int(i) % 2 != 0)]

C:
def even_odd_count(n):
    n = str(n)
    return [n.count('0'), n.count('1')]

D:
def even_odd_count(n):
    n = str(n)
    return [n.count('2'), n.count('1')]

E:
def even_odd_count(n):
    n = str(n)
    return [sum(i % 2 == 0 for i in n), sum(i % 2 == 1 for i in n)]

F:
def even_odd_count(n):
    n = str(n)
    return [sum(i % 2 == 0 for i in n), sum(i % 2 != 0 for i in n)]

G:
def even_odd_count(n):
    n = str(n)
    return [n.count('0'), n.count('2')]

H:
def even_odd_count(n):
    n = str(n)
    return [sum(i % 2 == 0 for i in n), sum(i % 2 == 0 for i in n)]

I:
def even_odd_count(n):
    n = str(n)
    return [sum(i % 2 == 0 for i in n), sum(i % 2 != 0 for i in n)]

J:
def even_odd_count(n):
    n = str(n)
    return [sum(i % 2 == 0 for i in n), sum(i % 2 != 0 for i in n)]

K:
def even_odd_count(n):
    n = str(n)
    return [sum(i % 2 == 0 for i in n), sum(i % 2 == 0 for i in n)]

L:
def even_odd_count(n):
    n = str(n)
    return [sum(i % 2 == 0 for i in n), sum(i % 2 == 0 for i in n)]

M:
def even_odd_count(n):
    n = str(n)
    return [sum(i % 2 == 0 for i in n), sum(i % 2 == 0 for i in n)]

N:
def even_odd_count(n):
    n