from collections import defaultdict
def unique_sublists(lst):
    result = defaultdict(int)
    for sublst in lst:
        result[tuple(sublst)] += 1
    return dict(result)  # Convert back to regular dictionary