def expensive_items(items, n):
    items.sort(key=lambda x: x['price'], reverse=True)
    return items[:n]

print(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1))
# Output: [{'name': 'Item-2', 'price': 555.22}]

"""
This function works by sorting the list of items by price in descending order, and then returning the first n items from the sorted list.
"""

# 2
