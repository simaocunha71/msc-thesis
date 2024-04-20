"""
Write a function to find minimum k records from tuple list.  - in this case a verbatim copy of test cases
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
"""
import collections

def min_k(tuples, k):
    """
        : type tuples: List[Tuple]
            : type tuples: Collection of tuple.
            0-indexed.
            Each element is a tuple of two elements: (value, index)
            (e.g. [('Manjeet', 1), ('Akshat', 2), ('Akash', 3), ('Nikhil', 4)] --> [(5, 'Nikhil'), (4, 'Akash'), (3, 'Akshat'), (2, 'Manjeet')])
        : type k: int
            Number of elements to select.
            0 < k <= length(tuples)
    """
    index_dict = collections.defaultdict(list)
    for t in tuples:
        idx, val = t
        index_dict[idx].append((val, t))
    mini_vals = sorted(index_dict.values(), key=lambda x: x[1][2])
    return [x[0] for i, (_, j) in enumerate(mini_vals) if j < k]