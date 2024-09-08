def list_tuple(lst):
    return tuple(lst)

print(list_tuple([5, 10, 7, 4, 15, 3]))

#Solution 2
def list_tuple(lst):
    return lst,

print(list_tuple([5, 10, 7, 4, 15, 3]))

#Solution 3
def list_tuple(lst):
    return (lst[0], lst[1], lst[2], lst[3], lst[4], lst[5])

print(list_tuple([5, 10, 7, 4, 15, 3]))

#Solution 4
def list_tuple(lst):
    return lst[0], lst[1], lst[2], lst[3], lst[4], lst[5]

print(list_tuple([5, 10, 7, 4, 15, 3]))

#Solution 5
def list_tuple(lst):
    return tuple(lst[i] for i in range(len(lst)))

print(list_tuple([5, 10, 7, 4, 15, 3]))

#Solution 6
def list_tuple(lst):
    return tuple(iter(lst))

print(list_tuple([5, 10, 7, 4, 15, 3]))

#Solution 7
def list_tuple(lst):
    return tuple(lst.__iter__())

print(list_tuple([5, 10, 7, 4, 15, 3]))

#Solution 8
def list_tuple(lst):
    return tuple(lst.__next__() for _ in range(len(lst)))

print(list_tuple([5, 10, 7, 4, 15, 3]))

#Solution 9
def list_tuple(lst):