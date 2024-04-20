"""
Write a function that takes in a list of tuples and returns a dictionary mapping each unique tuple to the number of times it occurs in the list.
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
"""
from collections import Counter
def check_occurences(tuples):
    counter = Counter() # Counter() returns a dictionary of the tuple as key and the counts as values.
    for tuple in tuples:
        counter[tuple] += 1
    return {key: value for key, value in counter.items()}

# Driver code
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]) == \
     {(1, 3): 2, (2, 5): 2, (3, 6): 1}