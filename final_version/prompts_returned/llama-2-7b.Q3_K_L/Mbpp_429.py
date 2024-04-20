"""
Write a function to extract the elementwise and tuples from the given two tuples.
assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
"""

def _get_elementwise(a, b):
    return a[:] * b[:]

def _extract_tuples(a: tuple, b: tuple):
    def extract():
        return [tuple(_get_elementwise(a[i], b[j])) for i in range(len(a)) for j in range(len(b))]
    return extract()
