def remove_kth_element(lst: list, k: int) -> list:
    return lst[:k] + lst[k+1:]