import operator
def expensive_items(dataset, n):
    return sorted(dataset, key=operator.itemgetter('price'), reverse=True)[:n]