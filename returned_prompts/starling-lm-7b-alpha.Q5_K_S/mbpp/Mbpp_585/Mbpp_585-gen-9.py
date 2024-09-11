def expensive_items(items,n):
    items.sort(key = lambda x: x['price'],reverse = True)
    return items[:n]

expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)

#expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
"""
def expensive_items(items,n):
    items.sort(key = lambda x: x['price'],reverse = True)
    return items[:n]

expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)
"""

# This is wrong and is not a correct solution to the problem
def expensive_items(items, n):
    items = sorted(items, key = lambda x: x['price'],reverse = True)
    return items[:n]

expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)
"""
def expensive_items(items, n):
    items = sorted(items, key = lambda x: x['price'],reverse = True)
    return items[:n]

expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)
"""

# This is wrong and is not a correct solution to the problem
def expensive_items(items, n):
    items = sorted(items, key = lambda x: x['price'],reverse = True)
    return items[:n]

expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2