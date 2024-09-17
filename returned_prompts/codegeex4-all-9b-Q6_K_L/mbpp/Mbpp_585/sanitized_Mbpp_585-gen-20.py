def expensive_items(items, n):
    # Sort the items based on the price in descending order
    sorted_items = sorted(items, key=lambda x: x['price'], reverse=True)
    # Return the top n items
    return sorted_items[:n]