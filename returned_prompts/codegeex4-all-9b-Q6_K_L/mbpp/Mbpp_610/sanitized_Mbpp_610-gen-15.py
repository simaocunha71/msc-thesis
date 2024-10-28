def remove_kth_element(lst: list,k: int):
    return lst[:k-1] + lst[k:]