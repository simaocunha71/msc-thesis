def sum_squares(lst):
    return sum([i**2 if i%3 == 0 else i**3 if i%4 == 0 else i for i in lst])

B:
def sum_squares(lst):
    return sum(i**2 if i%3 == 0 else i**3 if i%4 == 0 else i for i in lst)

C:
def sum_squares(lst):
    return sum(i**2 if i%3 == 0 else i**3 for i in lst)

D:
def sum_squares(lst):
    return sum(i**2 if i%3 == 0 else i**3 if i%4 == 0 else i)

E:
def sum_squares(lst):
    return sum(i**2 if i%3 == 0 else i**3 if i%4 == 0 else i for i in lst) * 2

F:
def sum_squares(lst):
    return sum(i**2 if i%3 == 0 else i**3 if i%4 == 0 else i for i in lst)

G:
def sum_squares(lst):
    return sum(i**2 if i%3 == 0 else i**3 if i%4 == 0 else i for i in lst) / 2

H:
def sum_squares(lst):
    return sum(i**2 if i%3 == 0 else i**3 if i%4 == 0 else i for i in lst) - 2

I:
def sum_squares(lst):
    return sum(i**2 if i%3 == 0 else i**3 if i%4 == 0 else i for i in lst) + 2

J:
def sum_squares(lst):
    return sum(i**2 if i%3 == 0 else i**3 if i%4 == 0 else i for i in lst) * 3

K:
def sum_squares(lst):
    return sum(i**2 if i%3 == 0 else i**3 if i%4 == 0 else i for i in lst) / 3

L:
def sum_squares(lst):
    return sum(i**2 if i%3 == 0 else i**3 if i%4 == 0 else i for i in lst) - 3

M:
def sum_squares(lst):
    return sum(i**2 if i%3 == 0 else i**3 if i%4 ==