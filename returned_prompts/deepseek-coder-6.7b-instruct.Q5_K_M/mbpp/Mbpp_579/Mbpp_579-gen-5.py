def find_dissimilar(t1, t2):
    d = dict()
    for i in t1:
        d[i] = d.get(i, 0) + 1
    for i in t2:
        d[i] = d.get(i, 0) + 1
    return tuple(i for i in d if d[i] == 1)


print(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)))

"""
The function first creates a dictionary d, where the keys are the elements of the two tuples and the values are the counts of the elements in the two tuples.
Then it returns a tuple of the elements that appear exactly once in the two tuples.
"""

