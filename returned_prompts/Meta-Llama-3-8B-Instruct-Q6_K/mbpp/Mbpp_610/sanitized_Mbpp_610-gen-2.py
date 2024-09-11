def remove_kth_element(lst, k):
    return lst[:k-1] + lst[k:] if k > 0 and k <= len(lst) else lst