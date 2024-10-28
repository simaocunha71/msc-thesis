def max_product_tuple(lst):
    return max(abs(a*b) for a, b in lst) if len(lst) > 0 else None