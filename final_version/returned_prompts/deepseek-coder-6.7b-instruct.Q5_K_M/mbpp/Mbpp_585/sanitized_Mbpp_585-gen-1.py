def expensive_items(items, n):
    items.sort(key=lambda x: x['price'], reverse=True)
    max_price = items[0]['price']
    most_expensive_items = [item for item in items if item['price'] == max_price]
    return most_expensive_items[:n]