def max_product_tuple(tuples):
    return max(abs(a*b) for a, b in tuples)  # Assuming Python 3.5 or later