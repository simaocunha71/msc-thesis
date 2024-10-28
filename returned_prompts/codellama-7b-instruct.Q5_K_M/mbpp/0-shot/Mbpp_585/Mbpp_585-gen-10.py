def expensive_items(dataset,n):
    return sorted(dataset, key=lambda x: x['price'], reverse=True)[:n]


