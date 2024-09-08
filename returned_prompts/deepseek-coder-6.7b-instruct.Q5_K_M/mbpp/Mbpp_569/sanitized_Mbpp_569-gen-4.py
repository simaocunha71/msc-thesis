def sort_sublists(lst):
    result = []
    for sublist in lst:
        result.append(sorted(sublist))
    return result