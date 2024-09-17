from operator import itemgetter
def expensive_items(items,n):
    # Sort the items by price in descending order
    items.sort(key=itemgetter(1),reverse=True)
    # Return the first n items
    return items[:n]