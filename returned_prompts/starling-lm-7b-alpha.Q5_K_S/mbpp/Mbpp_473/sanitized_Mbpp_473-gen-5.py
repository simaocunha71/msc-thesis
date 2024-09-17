from collections import Counter
def tuple_intersection(*args):
    """
    Find the tuple intersection of elements in the given tuple list
    """
    counter = Counter()
    for tup in args:
        counter.update(tup)
    return tuple(counter.most_common(1)[0][1])