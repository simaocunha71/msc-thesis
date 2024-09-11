def tuple_intersection(*tuples):
    """
    Find the tuple intersection of elements in the given tuple list irrespective of their order.
    >>> tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)])
    {(4, 5), (3, 4), (5, 6)}
    """
    # Flatten all tuples into a single set
    all_elements = set(sum(tuples, []))

    # Create a new set to store the intersection
    intersection = set()

    # Iterate over all elements in the flattened set
    for element in all_elements:
        # If an element is in all tuples, it's part of the intersection
        if all(element in tup for tup in tuples):
            intersection.add(element)

    return intersection

# Unit Tests
from collections import defaultdict

def test_tuple_intersection():
    assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]) == set([(4, 5), (3, 4), (5, 6)])
    assert tuple_intersection([(1, 2), (3, 4), (5, 6), (7, 8)], [(1, 2), (3, 4), (5, 6), (7, 8)]) == set([(1, 2), (3, 4), (5, 6), (7, 8)])
    assert tuple_intersection([(1, 2), (3, 4), (5, 6), (7, 8)], [(1, 3), (4, 5), (6, 7), (8, 9)]) == set([])
    assert tuple_intersection([(1, 2), (3, 4), (5, 