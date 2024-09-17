def remove_kth_element(lst, k):
    if k < 1 or k > len(lst):
        raise ValueError("k is out of range")
    lst.pop(k-1)
    return lst