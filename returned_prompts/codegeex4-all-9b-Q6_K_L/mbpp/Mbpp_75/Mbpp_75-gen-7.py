def find_tuples(tuples: list, k: int) -> list:
    return [tup for tup in tuples if all(x % k == 0 for x in tup)]