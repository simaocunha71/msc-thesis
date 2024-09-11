"""
def drop_empty(d):
    return {key: val for key, val in d.items() if val}

# Test
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
"""

# Using Python's built-in `filter` function
from collections import defaultdict

def drop_empty(d):
    return defaultdict(list, {k: v for k, v in d.items() if v})

assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}

# Alternatively, you can use the `filter` function directly:
def drop_empty(d):
    return {k: v for k, v in filter(lambda t: t[1] != None, d.items())}

assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}

# Using a generator expression
def drop_empty(d):
    return {k: v for k, v in (k, v) for k, v in d.items() if v}

assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}

# Using dictionary comprehension
def drop_empty(d):
    return {k: v for k, v in d.items() if v}

assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}

# Using `filter` and `map` functions
def drop_empty(d):
    return {k: v for k, v in map(lambda t: t[0], filter(lambda t: t[1] != None, d.items()))}

assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})