def combinations_list(lst):
    results = [[]]
    for i in range(len(lst)):
        results.extend([subset + [lst[i]] for subset in results])
    return results