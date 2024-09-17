def expensive_items(dataset, n):
    data = sorted(dataset, key=lambda x: x['price'], reverse=True)[:n]
    return data