def extract_index_list(l1, l2, l3):
    # Find the intersection of the indices of the common elements.
    intersection = set(l1).intersection(set(l2)).intersection(set(l3))
    # Return a list of the common elements.
    return [x for x in intersection]



