from operator import itemgetter
def expensive_items(dataset,n):
    return sorted(dataset, key=itemgetter('price'), reverse=True)[:n]