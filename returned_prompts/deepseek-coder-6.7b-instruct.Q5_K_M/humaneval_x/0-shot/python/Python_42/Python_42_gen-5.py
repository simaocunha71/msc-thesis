

def incr_list(l: list):
    return [i + 1 for i in l]


print(incr_list([1, 2, 3]))
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))


# OR


def incr_list(l: list):
    for i in range(len(l)):
        l[i] += 1
    return l


print(incr_list([1, 2, 3]))
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))


# OR


def incr_list(l: list):
    return list(map(lambda x: x + 1, l))


print(incr_list([1, 2, 3]))
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))


# OR


def incr_list(l: list):
    return [x + 1 for x in l]


print(incr_list([1, 2, 3]))
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))


# OR


def incr_list(l: list):
    return [x+1 for x in l]


print(incr_list([1, 2, 3]))
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))


# OR


def incr_list(l: list):
    return list(map(lambda x: x+1, l))


print(incr_list([1, 2, 3]))
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0