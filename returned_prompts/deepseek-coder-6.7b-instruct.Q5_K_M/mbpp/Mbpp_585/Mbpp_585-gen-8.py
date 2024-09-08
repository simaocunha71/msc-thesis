
def expensive_items(items, n):
    items.sort(key=lambda x: x['price'], reverse=True)
    return items[:n]


print(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1))

#Output: [{'name': 'Item-2', 'price': 555.22}]

This function works by sorting the given list of dictionaries in descending order based on the 'price' value. It then returns the first n items from this sorted list. The returned list will contain the n most expensive items according to the 'price' field.
"""

"""

