def find_tuples(tuples, k):
    return [t for t in tuples if all(i % k == 0 for i in t)]

# TESTS
from itertools import product

def test_find_tuples():
    assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
    assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 7) == [(7, 9, 6)]
    assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 12) == [(6, 24, 12), (12, 18, 21)]
    assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 18) == [(12, 18, 21)]
    assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 24) == [(6, 24, 12)]

if __name__ == "__main__":
    test_find_tuples()
