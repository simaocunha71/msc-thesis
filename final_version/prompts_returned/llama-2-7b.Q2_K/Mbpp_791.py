"""
Write a function to remove tuples from the given tuple.
assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
"""

def remove_nested(tup):
    if not tup: return None
    elif isinstance(tup[0], tuple) or isinstance(tup[1],tuple):
        return [(x for x in tup[:2]] + [remove_nested(tup[2:])]
             else:
                yield from map(remove_nested,zip(*tup))
    else:
        yield remove_nested(tup)