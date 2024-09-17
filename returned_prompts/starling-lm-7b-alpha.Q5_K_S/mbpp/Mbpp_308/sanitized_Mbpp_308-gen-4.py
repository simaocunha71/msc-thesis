def large_product(list_one, list_two, num):
    """
    Parameters
    ----------
    list_one : list
        The first list.
    list_two : list
        The second list.
    num : int
        The number of largest products to find.

    Returns
    -------
    list
        The largest products of the two lists.
    """
    list_one = sorted(list_one, reverse=True)
    list_two = sorted(list_two, reverse=True)
    products = []
    for i in range(num):
        products.append(list_one[i] * list_two[i])
    return products