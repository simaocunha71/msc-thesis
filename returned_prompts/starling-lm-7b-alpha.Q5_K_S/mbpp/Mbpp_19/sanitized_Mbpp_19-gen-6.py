from collections import Counter
def test_duplicate(L):
    counter = Counter(L)
    return any(c > 1 for c in counter.values())