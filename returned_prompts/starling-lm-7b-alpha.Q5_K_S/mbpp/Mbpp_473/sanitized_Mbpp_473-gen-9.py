from collections import Counter
def tuple_intersection(*tuples):
    counter = Counter()
    for t in tuples:
        counter += Counter(t)
    return counter.most_common()