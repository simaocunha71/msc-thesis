def combinations_colors(color_list, n):
    # Import combinations from itertools
    from itertools import product
    # Use product to generate all combinations
    return list(product(*([color_list]*n)))