
def expensive_items(items, n):
    # Sort the items by price in descending order
    items.sort(key=lambda x: x['price'], reverse=True)

    # Return the n most expensive items
    return items[:n]

print(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1))


