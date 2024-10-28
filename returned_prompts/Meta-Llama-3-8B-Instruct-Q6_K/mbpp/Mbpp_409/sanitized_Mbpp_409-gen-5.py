def min_product_tuple(lst):
    result = float('inf')
    for pair in lst:
        result = min(result, pair[0] * pair[1])
    return result