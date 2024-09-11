"""
def interleave_lists(l1, l2, l3):
    return [x for l in [l1, l2, l3] for x in l]
"""

def interleave_lists(l1, l2, l3):
    return l1 + l2 + l3

def interleave_lists(l1, l2, l3):
    return l1[:] + l2[:] + l3[:]

def interleave_lists(l1, l2, l3):
    return l1 + l2 + l3

def interleave_lists(l1, l2, l3):
    return itertools.chain(l1, l2, l3)

def interleave_lists(l1, l2, l3):
    return (l1, l2, l3)

def interleave_lists(*args):
    return itertools.chain(*args)

def interleave_lists(l1, l2, l3):
    return l1[:] + l2[:] + l3[:]

def interleave_lists(*args):
    return itertools.chain(*args)

def interleave_lists(*args):
    return reduce(lambda a, b: a + b, args)

def interleave_lists(*args):
    return reduce(list.__add__, args)

def interleave_lists(*args):
    return functools.reduce(lambda a, b: a + b, args)

def interleave_lists(*args):
    return functools.reduce(list.__add__, args)

def interleave_lists(*args):
    return sum(args, [])

def interleave_lists(*args):
    return functools.reduce(lambda a, b: a + b, args)

def interleave_lists(*args):
    return functools.reduce(list.__add__, args)

def interleave_lists(*args):
    return itertools.chain(*args)

def interleave_lists(*args):
    return itertools.chain(*args)

def interleave_lists(*args):
    return itertools.chain(*args)

def interleave_