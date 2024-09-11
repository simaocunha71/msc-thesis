from collections import Counter
def count_reverse_pairs(arr):
    """
    Count the pairs of reverse strings in the given string list.
    """
    counter = Counter(arr)
    return sum(v//2 for v in counter.values() if v%2==1)