
def tuple_intersection(tuple_list: list) -> set:
    result = set()
    for tup in tuple_list:
        result.add(frozenset(tup))
    return set(frozenset.intersection(*result))


