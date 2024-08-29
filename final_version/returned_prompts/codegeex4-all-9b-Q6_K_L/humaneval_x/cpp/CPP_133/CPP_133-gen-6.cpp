def sum_squares(lst):
    lst = map(int, lst)
    return sum([i**2 for i in lst])

B:
def sum_squares(lst):
    return sum([i**2 for i in [int(i) for i in lst]])

C:
def sum_squares(lst):
    return sum([i**2 for i in list(map(int, lst))])

D:
def sum_squares(lst):
    return sum([int(i)**2 for i in lst])

E:
def sum_squares(lst):
    return sum([i**2 for i in list(map(int, lst))])

F:
def sum_squares(lst):
    return sum([int(i) ** 2 for i in lst])


