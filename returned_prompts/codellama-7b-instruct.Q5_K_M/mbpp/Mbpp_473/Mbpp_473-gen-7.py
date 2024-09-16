"""
def tuple_intersection(tuple_list):
    all_tuples = set()
    for tuples in tuple_list:
        all_tuples |= set(tuples)
    return set([t for t in all_tuples if all_tuples.count(t) == len(tuple_list)])
"""
