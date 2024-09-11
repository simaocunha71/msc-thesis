def index_elem(lst, elem):
    if elem in lst:
        return lst.index(elem)
    else:
        return -1


# Test
assert index