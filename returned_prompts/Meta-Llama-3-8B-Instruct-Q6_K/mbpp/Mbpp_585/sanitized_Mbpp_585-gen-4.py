from operator import itemgetter
def expensive_items(items,n):
    sorted_items = sorted(items, key=itemgetter('price'), reverse=True)
    return sorted_items[:n]  # return the n most expensive items