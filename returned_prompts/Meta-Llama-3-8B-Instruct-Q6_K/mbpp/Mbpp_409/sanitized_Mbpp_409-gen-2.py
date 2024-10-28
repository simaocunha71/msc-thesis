def min_product_tuple(tuples):
    return min(a*b for a, b in tuples)  # Python 3.x
    # return min([a*b for a, b in tuples])  # Python 2.x