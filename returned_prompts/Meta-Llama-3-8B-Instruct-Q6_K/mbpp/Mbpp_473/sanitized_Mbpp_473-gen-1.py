from collections import Counter
def tuple_intersection(tuples1, tuples2):
    counter1 = Counter(tuple(sorted(t)) for t in tuples1)
    counter2 = Counter(tuple(sorted(t)) for t in tuples2)
    return [tuple(sorted(t)) for t in set(tuples1) & set(tuples2) if counter1[tuple(sorted(t))] > 0 and counter2[tuple(sorted(t))] > 0]  # return the result as per the problem statement