"""
Write a function to find the union of the elements of two given tuples and output them in sorted order.
assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)
"""

def find_union(tuples):
    '''Union of sets of elements in tuples.'''
    out = []
    while len(tuples[0]) < len(tuples[1]):
        out.append(tuples[0][-1])
    for i in range(len(tuples)):
        if len(tuple) == 0:
            break
        else:
            if not (len(out) > 0 and out[-1] < tuples[i]):
                out.append(tuples[i][-1])
    return sorted(set(out))
