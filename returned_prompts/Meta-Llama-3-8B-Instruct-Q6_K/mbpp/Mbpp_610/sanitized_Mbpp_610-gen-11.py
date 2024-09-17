def remove_kth_element(lst, k):
    if k > len(lst):
        return lst  # or raise an exception, depending on your requirements
    lst.pop(k-1)
    return lst