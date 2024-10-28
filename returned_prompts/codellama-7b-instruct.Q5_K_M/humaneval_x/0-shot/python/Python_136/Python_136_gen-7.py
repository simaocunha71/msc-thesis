
def largest_smallest_integers(lst):
    largest = None
    smallest = None
    for i in lst:
        if i < 0 and (largest is None or i > largest):
            largest = i
        elif i > 0 and (smallest is None or i < smallest):
            smallest = i
    return (largest, smallest)

def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([-5, -3, 0, 2, 1, 3, 5]) == (-5, 1)

test_largest_smallest_integers()

