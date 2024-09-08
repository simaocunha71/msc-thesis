def expensive_items(data,n):
    data = sorted(data, key = lambda i: i['price'],reverse=True)
    return data[:n]