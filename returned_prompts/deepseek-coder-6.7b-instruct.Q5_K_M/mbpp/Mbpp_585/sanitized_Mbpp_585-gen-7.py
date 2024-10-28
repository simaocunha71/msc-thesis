def expensive_items(items, n):
    items.sort(key = lambda x: x['price'], reverse = True)
    return items[:n]