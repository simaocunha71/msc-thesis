from operator import itemgetter
def expensive_items(dataset, n):
    dataset.sort(key=itemgetter('price'), reverse=True)
    return dataset[:n]