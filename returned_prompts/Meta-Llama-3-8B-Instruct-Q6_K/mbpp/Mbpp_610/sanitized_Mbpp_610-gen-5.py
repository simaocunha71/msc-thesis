def remove_kth_element(lst, k):
    if k > len(lst):
        return "k is larger than the length of the list"
    return lst[:k-1] + lst[k:]