"""
Write a function to find the minimum product from the pairs of tuples within a given list.
assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
"""

def min_product_tuple(tuples):
    """ return minimum product from the pairs of tuples within a given list
        :param tuples: each tuple should contain two elements to form a pair.
                       tuples can be in any order.
        :return: find the minimum product from tuples as long as it contains 2 elements.
    """
    min_prod = None
    if not isinstance(tuples, list):
        raise TypeError('Argument list is required')
    for prod in itertools.combinations(*tuples):
        prod_sums = sum(prod)
        if (not min_prod or prod_sums < min_prod):
            min_prod = prod_sums
    return min_prod
