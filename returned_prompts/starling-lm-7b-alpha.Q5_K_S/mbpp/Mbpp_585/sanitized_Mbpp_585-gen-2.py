def expensive_items(items, n):
    """
    Finds the n most expensive items in a given dataset.

    Args:
        items (list): A list of dictionaries containing the name and price of items.
        n (int): The number of most expensive items to return.

    Returns:
        list: A list of dictionaries containing the names and prices of the most expensive items.
    """
    items.sort(key=lambda x: x['price'], reverse=True)
    return items[:n]