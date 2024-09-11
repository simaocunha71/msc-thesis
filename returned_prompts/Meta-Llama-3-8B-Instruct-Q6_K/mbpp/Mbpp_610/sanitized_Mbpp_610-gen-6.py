def remove_kth_element(lst, k):
    if k > len(lst):
        return "k is out of range"
    return lst[:k-1] + lst[k:]