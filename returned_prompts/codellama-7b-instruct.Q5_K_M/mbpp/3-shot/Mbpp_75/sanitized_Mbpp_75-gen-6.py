def find_tuples(tuple_list: list, k: int) -> list:
    return [tup for tup in tuple_list if all(i % k == 0 for i in tup)]