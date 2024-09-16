
def expensive_items(data, n):
    return sorted(data, key=lambda x: x['price'], reverse=True)[:n]

"""
Write a function to find the n most expensive items in a given dataset.

def expensive_items(data, n):
    # Sort the data by price
    data.sort(key=lambda x: x['price'], reverse=True)
    # Return the n most expensive items
    return data[:n]

"""

