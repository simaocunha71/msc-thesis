def find_dissimilar(tuple1, tuple2):
    for i in tuple1:
        if i not in tuple2:
            return i
    for i in tuple2:
        if i not in tuple1:
            return i

print(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)))





"""
def find_dissimilar(tuple1, tuple2):
    lst = []
    for i in tuple1:
        if i not in tuple2:
            lst.append(i)
    for i in tuple2:
        if i not in tuple1:
            lst.append(i)
    return lst

print(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)))
"""

"""
def find_dissimilar(tuple1, tuple2):
    lst = []
    for i in tuple1:
        if i not in tuple2:
            lst.append(i)
    for i in tuple2:
        if i not in tuple1:
            lst.append(i)
    return lst

print(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)))
"""

"""
def find_dissimilar(tuple1, tuple2):
    return [i for i in tuple1 if i not in tuple2] + [i for i in tuple2 if i not in tuple1]

print(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)))
"""

"""
def find_dissimilar(tuple1, tuple2):
    return list(set(tuple1) - set(tuple2)) + list(set(tuple2) - set(tuple1))

print(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)))
"""

"""
def find_diss