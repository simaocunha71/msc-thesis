def min_k(tup_list: list, k: int) -> list:
    min_k_tup = sorted(tup_list, key=lambda x: x[1])
    return min_k_tup[:k]