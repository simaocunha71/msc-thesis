def expensive_items(items, n):
    # Sort the items by price in descending order
    items.sort(key=lambda x: x['price'], reverse=True)

    # Return the n most expensive items
    return items[:n]