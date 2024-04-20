"""
Write a function that takes in a list of tuples and returns a dictionary mapping each unique tuple to the number of times it occurs in the list.
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
"""

def check_occurences(tuples):
    d = {}
    for tup in tuples:
        if tup[0] not in d.keys():
            n = len(d[tup[0]]) + 1
            d[tup[0]] = n
        else:
            d[tup[0]] += 1
    return d
