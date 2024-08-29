def expensive_items(data,n):
    data = sorted(data, key = lambda i: i['price'],reverse=True)
    return data[:n]

print(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1))

"""
This function will take a list of dictionaries as input, each dictionary represents an item and its price. It will sort the list in descending order based on the price and then return the first n items.
"""

"""
