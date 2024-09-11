from operator import itemgetter
def expensive_items(data, n):
    return sorted(data, key=itemgetter('price'), reverse=True)[:n]  # or sorted(data, key=lambda x: x['price'], reverse=True)[:n] for Python 3.9 and below