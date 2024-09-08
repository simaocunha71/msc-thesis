"""
def tuple_intersection(tuples):
    result = []
    for tup in tuples:
        tup = set(tup)
        if not result:
            result = tup
        else:
            result = result & tup
    return result

assert tuple_intersection([(3, 4),  (5, 6),  (9, 10),  (4, 5)])  == {(4, 5), (3, 4), (5, 6)}
assert tuple_intersection([(5, 4),  (3, 4),  (6, 5),  (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
"""

def tuple_intersection(tuples):
    result = []
    for tup in tuples:
        tup = set(tup)
        if not result:
            result = tup
        else:
            result = result & tup
    return result

assert tuple_intersection([(3, 4),  (5, 6),  (9, 10),  (4, 5)])  == {(4, 5), (3, 4), (5, 6)}
assert tuple_intersection([(5, 4),  (3, 4),  (6, 5),  (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
<jupyter_output>
<empty_output>
<jupyter_text>
